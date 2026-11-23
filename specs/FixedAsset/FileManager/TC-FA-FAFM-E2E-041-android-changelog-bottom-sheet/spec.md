---
id: TC-FA-FAFM-E2E-041-android-changelog-bottom-sheet
title: "Mobile: Changelog sebagai bottom sheet"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FAFM-04", "§4.6#p4"]
smoke: []
dependsOn: []
trace:
  "T-FAFM-04": [14, 15, 16, 18, 19, 33, 34]
  "§4.6#p4": [11, 13, 14, 15, 16, 22, 23, 27, 38]
anchor: [3, 25]
coverage:
  android: automated
---

# Mobile: Changelog sebagai bottom sheet

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-041-1: Asset `Toyota Avanza {runId}`, status `Active`, Group `Fleet`, ada di entitas aktor.
  - DU-041-2: File `damage-01-{runId}.jpg`, Source `Damaged Photo`, Category `Damaged`, Size `900.0 KB` dari 921600 byte, milik DU-041-1.
  - DU-041-3: File `repair-02-{runId}.jpg`, Source `Repair Photo`, Category `Damaged`, Size `880.0 KB` dari 901120 byte, milik DU-041-1.
  - Entri Changelog dibentuk oleh aksi spec ini: `Delete` untuk DU-041-2, `Delete` untuk DU-041-3, lalu `Permanently Delete` untuk DU-041-2, dalam urutan itu.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.
  - Retensi Recycle Bin bernilai `30 hari`.

## Test Steps

### Hapus dua file dari kartu tab Files
1. Ketuk tab `Damaged`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi kartu `damage-01-{runId}.jpg` tampil
4. Ketuk `[⋯]` pada kartu `damage-01-{runId}.jpg`
5. Ketuk `Delete`
6. Ketuk `[Delete]` pada dialog konfirmasi
7. Ketuk `[⋯]` pada kartu `repair-02-{runId}.jpg`
8. Ketuk `Delete`
9. Ketuk `[Delete]` pada dialog konfirmasi

### Changelog tampil sebagai bottom sheet berisi Card List
10. Ketuk ikon dengan label aksesibel `Changelog` pada header kartu Storage Usage
11. Verifikasi bottom sheet berjudul `Changelog` tampil
12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi entri Changelog tampil sebagai Card List
14. Verifikasi kartu entri `Delete` untuk `damage-01-{runId}.jpg` menampilkan File Name `damage-01-{runId}.jpg`
15. Verifikasi kartu entri `Delete` untuk `damage-01-{runId}.jpg` menampilkan Date menurut Date Format dan Time Format di Kondisi
16. Verifikasi kartu entri `Delete` untuk `damage-01-{runId}.jpg` menampilkan Modified By nama aktor dalam format `[First Name] [Last Initial]`

### Search menyaring kartu entri Changelog
17. Ganti isi kotak Search dengan `damage-01-{runId}.jpg`, tekan Enter
18. Verifikasi kartu entri `Delete` untuk `damage-01-{runId}.jpg` tampil
19. Verifikasi kartu entri `Delete` untuk `repair-02-{runId}.jpg` tidak tampil
20. Tutup bottom sheet Changelog

### Recycle Bin tampil sebagai bottom sheet dengan row action
21. Ketuk ikon dengan label aksesibel `Recycle Bin` pada header kartu Storage Usage
22. Verifikasi bottom sheet berjudul `Recycle Bin` tampil
23. Verifikasi Info `Files are permanently deleted after 30 days.` tampil
24. Ketik Search `{runId}`, tekan Enter
25. Verifikasi kartu `damage-01-{runId}.jpg` tampil
26. Ketuk `[⋯]` pada kartu `damage-01-{runId}.jpg`
27. Verifikasi menu aksi kartu memuat `Permanently Delete`
28. Ketuk `Permanently Delete`
29. Ketuk `[Permanently Delete]` pada dialog konfirmasi
30. Tutup bottom sheet Recycle Bin

### Urutan default entri Changelog sesudah Permanently Delete
31. Ketuk ikon dengan label aksesibel `Changelog` pada header kartu Storage Usage
32. Ketik Search `{runId}`, tekan Enter
33. Verifikasi kartu entri `Permanently Delete` untuk `damage-01-{runId}.jpg` tampil
34. Verifikasi urutan kartu entri dari atas ke bawah: `Permanently Delete` untuk `damage-01-{runId}.jpg`, `Delete` untuk `repair-02-{runId}.jpg`, `Delete` untuk `damage-01-{runId}.jpg`
35. Tutup bottom sheet Changelog

### Caption pada tab Disposed & Unmanaged Assets
36. Gulir daftar tab ke kanan sampai tab `Disposed & Unmanaged Assets` terlihat
37. Ketuk tab `Disposed & Unmanaged Assets`
38. Verifikasi caption `Asset data can only be deleted from the Asset menu.` tampil
