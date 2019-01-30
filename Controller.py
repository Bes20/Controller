class VoiceCommand:
    def __init__(self, channels):
        self.Channels = channels
        self.current_ch = 0

    def first_channel(self):
        return self.Channels[0]

    def last_channel(self):
        self.current_ch = len(self.Channels)-1
        return self.Channels[len(self.Channels)-1]

    def turn_channel(self, number_ch):
        self.current_ch = number_ch-1
        return self.Channels[self.current_ch]

    def next_channel(self):
        try:
            self.current_ch += 1
            return self.Channels[self.current_ch]

        except IndexError:
            self.current_ch = self.current_ch - len(self.Channels)
            return self.Channels[self.current_ch]

    def previous_channel(self):
        self.current_ch -= 1
        return self.Channels[self.current_ch]

    def current_channel(self):
        return self.Channels[self.current_ch]

    def is_exist(self, n):
        if type(n) == int:
            if len(self.Channels) <= n:
                return "No"
            else:
                return "Yes"
        elif type(n) == str:
            if n in self.Channels:
                return "Yes"
            else:
                return "No"


if __name__ == '__main__':
    CHANNELS = ['BBC', 'Discovery', 'TV1000']
    controller = VoiceCommand(CHANNELS)
    controller.is_exist(6)
    controller.turn_channel(3)
    controller.next_channel()
    controller.current_channel()
