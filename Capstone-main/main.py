from app import create_app

app = create_app()

if __name__ == '__main__':
    app.config['STATIC_PATH'] = 'app/static/'
    app.run(debug=False, host='0.0.0.0', port=8000)
