from aiosmtpd.controller import Controller


class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print("📨 Email received")
        print(f"From: {envelope.mail_from}")
        print(f"To: {envelope.rcpt_tos}")
        print("Raw message:\n", envelope.content.decode("utf8", errors="replace"))
        return "250 OK (message accepted)"


if __name__ == "__main__":
    controller = Controller(CustomSMTPHandler(), hostname="localhost", port=1025)
    controller.start()
    print("🚀 SMTP server running on localhost:1025")
    try:
        import asyncio

        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("🛑 Shutting down...")
        controller.stop()
