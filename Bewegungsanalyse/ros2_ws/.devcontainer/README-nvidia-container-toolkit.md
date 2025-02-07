# README - Installation der NVIDIA Container Toolkit unter Ubuntu

Dieses Dokument beschreibt die Schritte und Befehle, die notwendig sind, um den NVIDIA Container Toolkit unter Ubuntu zu installieren und in Docker zu integrieren.
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

---

## 1. Repository hinzufügen

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

**Hinweis**: Wenn du zusätzlich das *experimental* Repository benötigst, kannst du es einkommentieren:

```bash
sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

---

## 2. Pakete aktualisieren

```bash
sudo apt-get update
```

---

## 3. NVIDIA Container Toolkit installieren

```bash
sudo apt-get install -y nvidia-container-toolkit
```

---

## 4. Docker-Konfiguration anpassen

```bash
sudo nvidia-ctk runtime configure --runtime=docker
```

Dies erzeugt bzw. erweitert die Datei `/etc/docker/daemon.json` entsprechend.

---

## 5. Docker neu starten

```bash
sudo systemctl restart docker
```

---

### Abschließende Hinweise

- Nach der Installation können Container, die auf NVIDIA-Grafikkarten zugreifen, über Docker gestartet werden.
- Stelle sicher, dass der Docker-Dienst korrekt läuft und deine GPU-Treiber aktuell sind.
- Möchtest du die nicht mehr benötigten Pakete entfernen, kannst du optional `sudo apt autoremove` verwenden.

Viel Erfolg bei der Verwendung des NVIDIA Container Toolkit!
