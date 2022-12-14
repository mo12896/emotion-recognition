from typing import Protocol

import numpy as np
from deepface import DeepFace


class EmotionDetector(Protocol):
    def __init__(self, emotion_detector):
        ...

    def detect_emotions(self, image: np.ndarray) -> dict[str, float]:
        ...


class DeepFaceEmotionDetector:
    def __init__(self, emotion_detector=DeepFace):
        self.emotion_detector = emotion_detector

    def detect_emotions(self, image: np.ndarray) -> dict[str, float]:
        analyze = self.emotion_detector.analyze(image, actions=["emotion"])
        emotions = analyze["emotion"]
        return emotions
