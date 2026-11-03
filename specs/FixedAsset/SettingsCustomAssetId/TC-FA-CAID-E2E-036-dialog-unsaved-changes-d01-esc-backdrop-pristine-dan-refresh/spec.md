---
id: TC-FA-CAID-E2E-036-dialog-unsaved-changes-d01-esc-backdrop-pristine-dan-refresh
title: "Dialog D-01: Esc, Backdrop, Form Pristine, Setelah Save, Nilai Dikembalikan, dan Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-109
  - TC-FA-CAID-110
  - TC-FA-CAID-111
  - TC-FA-CAID-112
  - TC-FA-CAID-113
  - TC-FA-CAID-114
  - TC-FA-CAID-115
coverage:
  web: automated
---

# Dialog D-01: Esc, Backdrop, Form Pristine, Setelah Save, Nilai Dikembalikan, dan Refresh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) dan aset A1 sampai A5 (No 11), dipulihkan oleh hook `beforeEach` suite. Tidak ada data Dinamis.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan mengamati dialog `beforeunload` bawaan browser pada TC-FA-CAID-114 dan menerimanya (konfirmasi muat ulang) oleh harness (prasyarat tahap script yang disediakan tim FE/BE). Teks dan tombol dialog itu ditentukan browser dan tidak diasersi.
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Division Code tersimpan tercentang pada TC-FA-CAID-115 dan TC-FA-CAID-112 (Save sukses). Hook `after` suite memulihkan Company Alpha ke baseline B1. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-111: Form pristine, pindah tab tanpa D-01

1. Klik tab `Asset Name`
2. Verifikasi tab `Asset Name` terbuka langsung tanpa dialog `Unsaved Changes`
3. Klik tab `Custom Asset ID`

### TC-FA-CAID-109: Esc setara Cancel

4. Centang `Division Code` tanpa menekan `[Save]`
5. Klik tab `Asset Name`
6. Tekan `Esc`
7. Verifikasi dialog tertutup
8. Verifikasi pengguna tetap di tab `Custom Asset ID`
9. Verifikasi perubahan dipertahankan (checkbox `Division Code` tetap tercentang)

### TC-FA-CAID-110: Klik backdrop di luar D-01 diabaikan

10. Klik tab `Asset Name`
11. Klik area backdrop di luar dialog
12. Verifikasi dialog `Unsaved Changes` tetap terbuka dan tidak menutup

### TC-FA-CAID-114: Refresh dengan form dirty

13. Klik `[Cancel]` pada dialog
14. Tekan F5
15. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
16. Terima konfirmasi bawaan browser agar halaman dimuat ulang

### TC-FA-CAID-113: Nilai diubah lalu dikembalikan tetap dirty

17. Pilih Separator `- (Dash)`
18. Pilih kembali Separator `/ (Slash)`
19. Verifikasi tombol `[Save]` aktif
20. Klik tab `Asset Name`
21. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning) tampil
22. Klik `[Leave]`
23. Klik tab `Custom Asset ID`

### TC-FA-CAID-115: Refresh dengan form pristine atau setelah Save

24. Tekan F5
25. Verifikasi tidak ada konfirmasi bawaan browser pada refresh pertama
26. Verifikasi halaman dimuat ulang langsung pada refresh pertama
27. Centang `Division Code`
28. Klik `[Save]`
29. Tunggu aksi selesai
30. Tekan F5
31. Verifikasi tidak ada konfirmasi bawaan browser pada refresh kedua
32. Verifikasi halaman dimuat ulang langsung pada refresh kedua

### TC-FA-CAID-112: Setelah Save sukses, pindah tab tanpa D-01

33. Atur konfigurasi Company Alpha ke baseline B1 (seed API), lalu muat ulang halaman
34. Centang `Division Code`
35. Klik `[Save]`
36. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
37. Klik tab `Asset Name`
38. Verifikasi tab `Asset Name` terbuka langsung tanpa dialog `Unsaved Changes`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 38 langkah, di atas smell 35 langkah. Alasan: seluruhnya satu topik dan satu kelas harness (dialog D-01 dan konfirmasi `beforeunload` pada form konfigurasi), tanpa kelas lain; memisahkannya hanya menambah login, hook, dan pembukaan halaman yang sama.
- Urutan TC di spec: TC-FA-CAID-111, TC-FA-CAID-109, TC-FA-CAID-110, TC-FA-CAID-114, TC-FA-CAID-113, TC-FA-CAID-115, TC-FA-CAID-112. Form dirty dan dialog dari langkah 4 dan 10 dipakai ulang oleh TC-FA-CAID-110 dan TC-FA-CAID-114 karena aksi pembuka mereka identik (centang `Division Code` tanpa Save); TC-FA-CAID-115 dan TC-FA-CAID-112 yang menyimpan konfigurasi berada di akhir (S-10).
- Langkah penghubung: langkah 3, 23 (kembali ke tab Custom Asset ID), langkah 13 (`[Cancel]` menutup dialog sebelum TC berikutnya), langkah 22 (`[Leave]` sesudah `Verifikasi` dialog pada langkah 21, S-08), langkah 29 (tunggu aksi selesai karena langkah berikutnya memuat ulang halaman), dan langkah 33 (pemulihan baseline lewat seed).
- Langkah 14 sampai 16 menangani dialog `beforeunload` sebagai objek uji TC-FA-CAID-114; langkah 30 menekan F5 sesudah Save sehingga tidak memunculkan konfirmasi (objek uji TC-FA-CAID-115).
- Spec berakhir dengan form pristine (Save sukses lalu pindah tab).
- Pembagian TC lintas spec: TC-FA-CAID-104 sampai 108 ada di spec 035.
- Temuan untuk QA:
  - TC-FA-CAID-114 dan TC-FA-CAID-115 mengasersi dialog `beforeunload` bawaan browser; TC tidak menyebut kemampuan harness untuk mengamati dan menerima dialog itu, sehingga dicatat sebagai kebutuhan tim FE di Prerequisites.
  - TC-FA-CAID-115 langkah 2 tidak menyebut toast Save; spec menunggu aksi selesai tanpa asersi toast.
  - Post Condition TC-FA-CAID-109 sampai 115 tidak diasersi karena TC tidak memberi langkah observasinya.
