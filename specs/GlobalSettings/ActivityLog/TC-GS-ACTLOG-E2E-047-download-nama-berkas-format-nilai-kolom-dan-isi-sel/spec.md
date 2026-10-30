---
id: TC-GS-ACTLOG-E2E-047-download-nama-berkas-format-nilai-kolom-dan-isi-sel
title: "Download: Nama Berkas, Format Nilai, Kolom, dan Isi Sel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-125
  - TC-GS-ACTLOG-129
  - TC-GS-ACTLOG-130
  - TC-GS-ACTLOG-131
  - TC-GS-ACTLOG-133
  - TC-GS-ACTLOG-134
coverage:
  web: automated
---

# Download: Nama Berkas, Format Nilai, Kolom, dan Isi Sel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession). Spec tidak mengganti akun, sehingga sesi akhir tetap akun default suite.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun admin pelaku aksi sumber: `Hendra Pratama` (Total Control Client A), fixture `Fixture.activityLog.adminHendra` (email ditetapkan tim FE); password dari `Spectra.env.GS_HENDRA_PASSWORD`. Dipakai di hook `before` lewat sesi API untuk membuat Brand sehingga muncul baris User Action dengan Modified By `Hendra P`.
- Subjek log literal (Population D-04, S-12): user `John Doe` (EMP001; Position `Staff-047` dan Division `Marketing-047` milik seeding spec ini; tidak diasersi, hanya dibuat bila field wajib, dan mengikuti siklus hidup `John Doe` sehingga tidak dihapus); password dari `Spectra.env.ACTLOG_PASSWORD`. Nama literal disengaja: TC-GS-ACTLOG-125 mengasersi nama lengkap di berkas terhadap singkatan di tabel (`John D`, `Hendra P`), dan suffix `{runId}` akan mengubah singkatan itu. Syarat D-04: seeding idempotent (dilewati bila sudah ada), tidak dihapus, suite serial, dan `John Doe` serta `Hendra Pratama` bukan target aksi tulis spec lain.
- Data Dinamis (suffix `{runId}-047`):
  - Entri Session `John Doe`: login `John Doe` lewat sesi API (alur Auth) di hook `before`.
  - Entri User Action oleh `Hendra Pratama`: di hook `before`, `Hendra Pratama` login lewat sesi API lalu membuat Brand `Brand Hendra {runId}-047` lewat API (aksi nyata modul Brand); Brand dihapus lewat API oleh akun aktor di hook `after` tanpa berasumsi seeding berhasil penuh.
  - User tanpa Position `User Format {runId}-047` (Division `Operations {runId}-047`) dibuat lewat API di hook `before`; user dan Division dihapus di hook `after`.
  - Entri bercap waktu tetap untuk TC-GS-ACTLOG-133 (baris log hasil seed BE, tanpa record Brand sungguhan sehingga tidak ada cleanup Brand; entri log tidak dapat dihapus): entri Session milik `User Format {runId}-047` tersimpan UTC `14 Jul 2026, 17:30`, dan entri User Action Create Brand `Brand Format {runId}-047` tersimpan UTC `14 Jun 2026, 07:05` dengan Old Value `—`.
- Volume log: log Client A pada Tab Session dan Tab User Action tidak melebihi 5.000 baris (precondition TC-GS-ACTLOG-131), dijamin tim FE/BE (reset log Client A sebelum run atau pemantauan jumlah baris); bila terlampaui TC-GS-ACTLOG-131 tidak valid; seed volume hanya ada di entitas Client Volume spec 050.
- Kemampuan teknis (disediakan tim FE/BE):
  - Kelas binary buffer (prinsip 13f): menangkap berkas unduhan browser ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (baris header, urutan kolom, nilai sel, nama sheet XLSX). Berkas unduhan dihapus di hook `after`.
  - Seed BE untuk dua entri bercap waktu tetap pada TC-GS-ACTLOG-133 (entri hasil aksi nyata tidak dapat dibuat bercap UTC masa lalu); mekanisme seed tidak disebut di TC, PRD, atau LLD.
  - Membaca dan mengubah General Settings (Date Format, Time Format, Time Zone) lewat API.
- State global yang diubah dan dipulihkan:
  - General Settings (Date Format, Time Format, Time Zone): nilai awal dibaca lewat API di hook `before`, diatur di langkah 28, dipulihkan di langkah 38; hook `after` memulihkan lagi sebagai cadangan.
  - Konfigurasi Setup Column Tab Session dan Tab User Action: dikembalikan ke default di langkah 49 dan 51; hook `after` mengembalikan ke default sebagai cadangan.
- Suite serial (`parallel: false`) karena spec mengubah General Settings dan konfigurasi Setup Column.
- Hook `beforeEach`: kembali ke layar Global Settings > Activity Log > Session.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-129: Nama berkas dan ekstensi mengikuti pilihan CSV, kedua tab

2. Klik icon Download
3. Verifikasi Overlay Download memuat opsi `Download as CSV`
4. Verifikasi Overlay Download memuat opsi `Download as XLSX`
5. Klik `Download as CSV`
6. Verifikasi tab Session mengunduh berkas `Activity-Log-Session.csv`
7. Klik tab "User Action", klik icon Download, lalu klik `Download as CSV`
8. Verifikasi tab User Action mengunduh berkas `Activity-Log-User-Action.csv`

### TC-GS-ACTLOG-125: Sel User dan Modified By di berkas Download berisi nama lengkap, kedua tab

9. Buka isi berkas `Activity-Log-Session.csv` yang diunduh pada langkah 5, lalu periksa sel User baris `John Doe`
10. Verifikasi sel User baris `John Doe` bernilai `John Doe`
11. Verifikasi sel User baris `John Doe` bukan `John D`
12. Buka isi berkas `Activity-Log-User-Action.csv` yang diunduh pada langkah 7, lalu periksa sel Modified By baris `Hendra Pratama`
13. Verifikasi sel Modified By baris `Hendra Pratama` bernilai `Hendra Pratama`
14. Verifikasi sel Modified By baris `Hendra Pratama` bukan `Hendra P`

### TC-GS-ACTLOG-130: Nama berkas dan ekstensi mengikuti pilihan XLSX, kedua tab

15. Klik tab "Session", klik icon Download, lalu klik `Download as XLSX`
16. Verifikasi tab Session mengunduh berkas `Activity-Log-Session.xlsx`
17. Klik tab "User Action", klik icon Download, lalu klik `Download as XLSX`
18. Verifikasi tab User Action mengunduh berkas `Activity-Log-User-Action.xlsx`
19. Verifikasi nama sheet berkas `Activity-Log-User-Action.xlsx` sama dengan nama file tanpa ekstensi, yaitu `Activity-Log-User-Action`

### TC-GS-ACTLOG-131: Download berhasil tidak menampilkan toast sukses, kedua tab

20. Klik tab "Session", klik icon Download, klik `Download as CSV`, lalu amati layar
21. Verifikasi tab Session: tidak ada toast sukses
22. Verifikasi tab Session: tidak ada notifikasi in-app
23. Verifikasi tab Session: berkas terunduh langsung
24. Klik tab "User Action", klik icon Download, klik `Download as XLSX`, lalu amati layar
25. Verifikasi tab User Action: tidak ada toast sukses
26. Verifikasi tab User Action: tidak ada notifikasi in-app
27. Verifikasi tab User Action: berkas terunduh langsung

### TC-GS-ACTLOG-133: Format nilai di berkas export, tanggal ikut General Settings dan nilai kosong menjadi `-`

28. Atur General Settings lewat API: Date Format `DD/MM/YY`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`
29. Muat ulang halaman, lalu buka Global Settings > Activity Log > Session
30. Klik icon Download, klik `Download as CSV`, buka isi berkas yang terunduh, lalu periksa baris entri Session milik `User Format {runId}-047` (tersimpan UTC `14 Jul 2026, 17:30`)
31. Verifikasi sel Date baris entri tersebut memuat tanggal `15/07/26`
32. Verifikasi sel Date baris entri tersebut memuat jam `00:30`
33. Verifikasi sel Position baris entri tersebut bernilai `-` (tanda hubung tunggal, bukan kosong, bukan `—`, bukan `null`)
34. Klik tab "User Action", klik icon Download, klik `Download as CSV`, buka isi berkas yang terunduh, lalu periksa baris entri Create Brand `Brand Format {runId}-047` (tersimpan UTC `14 Jun 2026, 07:05`)
35. Verifikasi sel Date baris entri tersebut memuat tanggal `14/06/26`
36. Verifikasi sel Date baris entri tersebut memuat jam `14:05`
37. Verifikasi sel Old Value baris entri tersebut bernilai `-`
38. Pulihkan Date Format, Time Format, dan Time Zone General Settings ke nilai awal yang dibaca di hook `before`

### TC-GS-ACTLOG-134: Urutan dan nama kolom di berkas mengikuti tabel, kedua tab

39. Klik tab "Session", lalu buka Popup Setup Column lewat `⋯` pada header kolom Actions
40. Seret kolom Activity ke posisi paling atas, lalu klik [Save]
41. Tunggu aksi Save selesai (Popup Setup Column tertutup)
42. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
43. Verifikasi baris header berkas Tab Session berurutan `Activity`, `Date`, `User`, `Employee ID`, `Position`, `Division`, `Status`, `Note`, `IP Address`, `Device / Browser`
44. Klik tab "User Action", lalu buka Popup Setup Column lewat `⋯` pada header kolom Actions
45. Seret kolom Object ke posisi paling atas, lalu klik [Save]
46. Tunggu aksi Save selesai (Popup Setup Column tertutup)
47. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
48. Verifikasi baris header berkas Tab User Action berurutan `Object`, `Date`, `Action`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`

### Pemulihan state antar TC

49. Tab User Action: buka Popup Setup Column, klik [Reset to Default], lalu klik [Save]
50. Tunggu aksi Save selesai (Popup Setup Column tertutup)
51. Klik tab "Session", buka Popup Setup Column, klik [Reset to Default], lalu klik [Save]
52. Tunggu aksi Save selesai (Popup Setup Column tertutup)

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`. Mode: FE+BE. Kelas binary buffer (prinsip 13f): isi berkas CSV/XLSX, nama, header, dan format nilai dipisah dari kegagalan export (spec 049), volume threshold (spec 050), dan cakupan baris (spec 048).
- P-5 (b): TC-GS-ACTLOG-133 (format tanggal General Settings di berkas) adalah objek-uji ringan kelas h pada permukaan berkas, satu TC kelas h di spec ini; General Settings dipulihkan di langkah 38 dan hook `after`.
- Population D-04 (S-12): `John Doe` dan `Hendra Pratama` bernama literal karena asersi bergantung pada singkatan nama; seeding idempotent, tidak dihapus, suite serial, bukan target aksi tulis spec lain.
- Urutan TC dalam spec: 129, 125, 130, 131, 133, 134. TC-GS-ACTLOG-125 membaca berkas hasil unduhan TC-GS-ACTLOG-129 (langkah 5 dan 7) tanpa unduh ulang, karena state tabel keduanya identik (tanpa Search dan Filter, semua kolom, urutan default), sehingga langkah "unduh Download as CSV" TC-GS-ACTLOG-125 terpenuhi oleh unduhan itu. TC-GS-ACTLOG-133 dan 134 mengubah state global (General Settings, Setup Column) sehingga ditaruh paling akhir dan dipulihkan.
- Blok per TC memuat kedua tab sesuai pemetaan TC, sehingga pindah tab berulang (langkah 7, 15, 17, 20, 24, 34, 39, 44, 51).
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab "Session" dan "User Action" antar TC; langkah 29 (muat ulang agar format baru dimuat); langkah 38 (memulihkan General Settings); langkah 41, 46, 50, dan 52 (Tunggu aksi Save selesai, bagian 8b butir 8); langkah 49 dan 51 (mengembalikan Setup Column ke default; hook `after` sebagai cadangan).
- Urutan langkah TC-GS-ACTLOG-131 mengikuti urutan state (bagian 8b butir 11): absence toast sukses dan notifikasi in-app diasersi segera setelah pemicu dan sebelum asersi berkas terunduh; pemicu (klik pilihan format) menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas.
- Asersi tambahan di luar Expected TC: tidak ada. Langkah 3 dan 4 memecah satu butir Expected TC-GS-ACTLOG-129 menjadi satu `Verifikasi` per opsi overlay (S-01).
- Spec di atas smell 35 langkah (52 langkah). Alasan: seluruh blok berkelas satu harness (binary buffer) dan berdiri sendiri; kegagalan satu blok TC tidak membuat blok lain kehilangan makna. State yang diubah (General Settings, Setup Column) dipulihkan sebelum blok berikutnya, dan tiap TC mencakup dua tab dengan Expected bermajemuk yang dipecah per klausa (S-01).
- Dependensi TC-GS-ACTLOG-134 pada TC-GS-ACTLOG-97 dan TC-GS-ACTLOG-184 (memindahkan kolom lewat Popup Setup Column) dipenuhi dengan menyalin langkah pemindahannya (langkah 39 sampai 40 dan 44 sampai 45).
- Pembagian TC lintas spec: TC-GS-ACTLOG-122, 123, 124, 127, 128, dan 135 ada di spec 048; TC-GS-ACTLOG-132 di spec 049; TC-GS-ACTLOG-136 dan 137 di spec 050.
- Temuan untuk QA:
  - TC-GS-ACTLOG-130: nama sheet XLSX hanya disebut untuk Tab User Action; nama sheet Tab Session tidak diasersi.
  - TC-GS-ACTLOG-131: Expected tidak menyebut nama berkas; spec hanya mengasersi berkas terunduh langsung.
  - TC-GS-ACTLOG-133: mekanisme membuat entri bercap UTC masa lalu tidak ada di TC, PRD, atau LLD; ditulis sebagai kemampuan seed BE tanpa endpoint (S-13). Expected "sel Date memuat tanggal dan jam" tidak menyatakan apakah satu sel; spec memecah menjadi dua `Verifikasi`.
  - TC-GS-ACTLOG-125: TC tidak menyebut cara menemukan baris di berkas; spec mencari lewat nilai sel User atau Modified By.
  - TC-GS-ACTLOG-125: akun admin `Hendra Pratama` (fixture `adminHendra`, email ditetapkan tim FE) dan user `John Doe` disediakan tim FE.
