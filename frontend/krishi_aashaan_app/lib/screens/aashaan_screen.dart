import 'package.flutter/material.dart';

class AashaanScreen extends StatefulWidget {
  const AashaanScreen({Key? key}) : super(key: key);

  @override
  State<AashaanScreen> createState() => _AashaanScreenState();
}

class _AashaanScreenState extends State<AashaanScreen> {
  // State variables for speech recognition will go here
  bool _isListening = false;
  String _text = 'Press the button and start speaking...';

  @override
  Widget build(BuildContext context) {
    // This screen is for voice-powered farm diary entries.
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Icon(Icons.record_voice_over, size: 60, color: Colors.red),
            const SizedBox(height: 20),
            const Text(
              'Krishi Diary',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 10),
            Text(
              _text,
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 16),
            ),
            const Spacer(),
            FloatingActionButton(
              onPressed: () {
                // TODO: Implement speech-to-text functionality
                setState(() {
                  _isListening = !_isListening;
                  if (_isListening) {
                    _text = "Listening... tap again to stop.";
                  } else {
                    _text = "Today I bought fungicide for 250 rupees. (Simulated)";
                  }
                });
              },
              child: Icon(_isListening ? Icons.mic_off : Icons.mic),
            ),
          ],
        ),
      ),
    );
  }
}
