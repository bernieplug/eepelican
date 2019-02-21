if [ ! -f "messages-$1.pot" ]; then
    pybabel extract --mapping babel.cfg --output "messages.pot" ./
fi

if [ ! -f "translations/es/LC_MESSAGES/messages.po" ]; then
    pybabel init --input-file messages.pot --output-dir translations/ --locale $1 --domain messages
else
    pybabel update --input-file messages.pot --output-dir translations/ --locale $1 --domain messages
fi

