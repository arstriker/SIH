import 'package.flutter/material.dart';

class NottamScreen extends StatefulWidget {
  const NottamScreen({Key? key}) : super(key: key);

  @override
  State<NottamScreen> createState() => _NottamScreenState();
}

class _NottamScreenState extends State<NottamScreen> {
  // State variable for the image will go here
  // File? _image;

  @override
  Widget build(BuildContext context) {
    // This screen is for the AI-powered visual diagnosis.
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Icon(Icons.linked_camera, size: 60, color: Colors.teal),
            const SizedBox(height: 20),
            const Text(
              'Visual Diagnosis (Nottam)',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 20),
            Container(
              height: 200,
              width: 200,
              color: Colors.grey[300],
              child: const Center(
                child: Text('Image preview appears here'),
              ),
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton.icon(
                  onPressed: () {
                    // TODO: Implement gallery access
                  },
                  icon: const Icon(Icons.photo_library),
                  label: const Text('Gallery'),
                ),
                ElevatedButton.icon(
                  onPressed: () {
                    // TODO: Implement camera access
                  },
                  icon: const Icon(Icons.camera_alt),
                  label: const Text('Camera'),
                ),
              ],
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // TODO: Implement API call to /diagnose
              },
              style: ElevatedButton.styleFrom(
                minimumSize: const Size(double.infinity, 40),
              ),
              child: const Text('Get Diagnosis'),
            ),
          ],
        ),
      ),
    );
  }
}
