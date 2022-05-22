import yfinance as yf
from stocks import stock_list
import smtplib
import ssl
from email.message import EmailMessage
from secrets import EMAIL_PASSWORD, EMAIL_USERNAME

def getClosingPrice(ticker):
    """
    @param ticker: string
    @returns: closing price of given ticker
    """
    t = yf.Ticker(ticker)

    hist = t.history(period="1d")

    #print(hist.Close[0])

    return hist.Close[0]


def sendAlert(stock):
    """
    @param stock: StockDef class
    """
    port = 465 # ssl port
    recieverEmail = "" # enter your email here
    subject = f"Subject: {stock.company} Alert\n\n"
    message = f"Current price has closed higher than {stock.desiredPrice}"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com", port, context=context) as server:
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, recieverEmail, subject + message)


def main():
    for stock in stock_list:
        previousDayClosingPrice = getClosingPrice(stock.ticker)
        if previousDayClosingPrice >= stock.desiredPrice:
            sendAlert(stock)


if __name__ == "__main__":
    main()
