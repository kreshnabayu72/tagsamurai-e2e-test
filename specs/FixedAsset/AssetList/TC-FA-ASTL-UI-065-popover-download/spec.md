---
id: TC-FA-ASTL-UI-065-popover-download
title: "Popover Download dan kegagalannya"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["T-05", "§5#r6", "§6#r9", "EB-DL-2@tabel-all-assets", "EB-DL-5"]
smoke: []
dependsOn: []
trace:
  "T-05": 9
  "§5#r6": [4, 5, 17, 18, 19]
  "§6#r9": [9, 13]
  "EB-DL-2@tabel-all-assets": [4, 5, 9]
  "EB-DL-5": [17, 18, 19]
anchor: []
coverage:
  web: automated
---
# Popover Download dan kegagalannya

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Popover Download
- Data:
  - DU-065-1: Aset pada tabel: Name `Printer Laser - 1`, Asset ID `AST-0031`, Status `Not Paired Yet`.
  - DU-065-2: Hasil filter di atas ambang: jumlah baris `5.001 baris`.
- Kondisi:
  - K1: tabel memuat DU-065-1 dan unduhan berhasil.
  - K2: tabel memuat DU-065-1 dan unduhan gagal karena error server.
  - K3: tabel memuat DU-065-1 dan unduhan gagal karena timeout.
  - K4: hasil filter memuat DU-065-2 dan berkas baru siap setelah layar loading tampil.

## Test Steps

### Unduhan berhasil tanpa toast sukses
1. Tampilkan Popover Download dengan kondisi K1
2. Klik ikon Download
3. Klik `Download as CSV`
4. Verifikasi unduhan berkas `All-Assets` dimulai
5. Verifikasi tidak ada toast sukses

### Unduhan gagal karena error server
6. Tampilkan Popover Download dengan kondisi K2
7. Klik ikon Download
8. Klik `Download as CSV`
9. Verifikasi toast `Error, failed to download All-Assets.` tampil

### Unduhan gagal karena timeout
10. Tampilkan Popover Download dengan kondisi K3
11. Klik ikon Download
12. Klik `Download as XLSX`
13. Verifikasi toast `Connection problem. Please try again.` tampil

### Layar loading pada unduhan besar
14. Tampilkan Popover Download dengan kondisi K4
15. Klik ikon Download
16. Klik `Download as XLSX`
17. Verifikasi layar loading tampil sampai berkas siap
18. Verifikasi tidak ada toast informasional maupun notifikasi
19. Verifikasi layar loading hilang dan unduhan berkas `All-Assets` dimulai
