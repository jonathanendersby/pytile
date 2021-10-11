from swarm.tile import TileSerial
import settings
from serial.tools.list_ports import comports


def __main__():
    tile_port = None
    try:
        if settings.SWARM_TILE_PORT is None:
            raise AttributeError
        else:
            tile_port = settings.SWARM_TILE_PORT

    except AttributeError:
        print('Auto Detecting Port...')
        for port in comports():
            if '2102N' in port.description:
                tile_port = port.device
                break
        if not tile_port:
            print('Unable to auto detect Tile port. Have you got it plugged in? '
                  'Have you set the jumper to bypass the Feather?')
            quit()

    print('Connecting to', tile_port)
    tile = TileSerial()
    tile.set_logging(True)
    tile.connect(tile_port)
    tile.write_read('$DT 0', expect='$DT OK')  # Turn off datetime unsolicited messages
    tile.write_read('$GN 0', expect='$GN OK')  # Turn off GNSS unsolicited messages

    print('Tile Firmware Version:')
    print(tile.get_firmware_version())

    print('Current GPS Time (UTC):')
    print(tile.get_gps_time())
    print('')
    gps_stats = tile.get_gps_stats()
    print(gps_stats.verbose())
    print(tile.get_message_count(), 'unread messages.')

    print('\n10 second monitor running... (Look in tile.log)')
    tile.read_monitor(seconds=10)

    # Send a message - setting defaults to False to avoid sending by mistake.
    if settings.SWARM_EXAMPLE_SENDS_A_TEST_MESSAGE:
        msg_id = tile.send_swarm_message('This is a test message sent from the Swarm Python Module',
                                         application_id='5555')
        print(msg_id)

__main__()
