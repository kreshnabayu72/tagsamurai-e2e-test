---
id: TC-FA-CAID-E2E-042-pencatatan-log-absence-tanpa-entri
title: "Pencatatan Log Absence: Zero-Delta, No-Op, Mass Update, dan Save Ditolak Tanpa Entri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-72
  - TC-FA-CAID-246
  - TC-FA-CAID-247
  - TC-FA-CAID-252
coverage:
  web: automated
---

# Pencatatan Log Absence: Zero-Delta, No-Op, Mass Update, dan Save Ditolak Tanpa Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`, untuk TC-FA-CAID-72, TC-FA-CAID-246, dan TC-FA-CAID-247. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. TC-FA-CAID-252 memakai Total Control `Company V07 65` (Pre-setup No 19); email akun disediakan tim FE/BE (Pre-setup No 19), password `Spectra.env.FA_V0765_TC_PASSWORD`, dan ganti akun ditulis sebagai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) dan aset A1 sampai A5 (No 11), dipulihkan oleh hook `beforeEach` suite; `Company V07 65` dengan satu aset Draft, Group Code `GRP-LONG-000001`, Category Code `CAT-LONG-000001`, Asset Name Code `AST-LONG-000001`, Separator `- (Dash)`, formula tanpa Purchase Date, dan Division Code `DIVISION-ABC-15` (No 19). General Settings Date Format `dd/MM/yy` dan Time Format 24 jam (No 27): dipakai sebagai precondition TC, tidak diasersi.
- Tabel "Aset yang diperiksa" (Company Alpha, baseline B1):

  | Aset | Asset ID awal |
  |---|---|
  | A1 | `JKT/LAP/T490/0926/1` |
  | A2 | `JKT/LAP/T490/0926/2` |
  | A3 | `JKT/LAP/T490/0000/3` |

- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) serta nilai Modified By dan Last Updated konfigurasi sebelum aksi (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Separator Company Alpha menjadi `- (Dash)` pada TC-FA-CAID-247 dan Asset ID aset berubah. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5, dan mengembalikan `Company V07 65` ke seed awal. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-72: Save zero-delta dengan toast netral

1. Pilih Separator `- (Dash)`
2. Pilih kembali Separator `/ (Slash)`
3. Verifikasi tombol `[Save]` tetap aktif walau nilai sama dengan nilai tersimpan
4. Klik `[Save]`
5. Verifikasi toast netral `No changes to save.` tampil
6. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tidak tampil
7. Verifikasi tombol `[Save]` kembali disabled
8. Buka Fixed Asset > Assets > All Assets
9. Verifikasi Asset ID A1, A2, A3 tetap `JKT/LAP/T490/0926/1`, `JKT/LAP/T490/0926/2`, `JKT/LAP/T490/0000/3`
10. Untuk setiap aset pada tabel "Aset yang diperiksa" lakukan langkah 11 sampai 13
11. Buka Detail aset > tab `Histori Aset`
12. Verifikasi header Detail aset menampilkan Asset ID awal aset pada tabel
13. Verifikasi tidak ada entri riwayat Asset ID baru pada aset

### TC-FA-CAID-246: Edit No-Op menulis nol entri log di tiga surface

14. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface serta nilai Modified By dan Last Updated konfigurasi
15. Pilih Separator `- (Dash)` lalu pilih kembali `/ (Slash)`
16. Klik `[Save]`
17. Verifikasi toast netral `No changes to save.` tampil
18. Verifikasi Modified By dan Last Updated konfigurasi tidak berubah dibanding baseline
19. Buka Modal Changelog: Custom Asset ID
20. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
21. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
22. Verifikasi jumlah entri System Log tidak bertambah dibanding baseline
23. Buka Fixed Asset > Activity Log > tab User Action
24. Verifikasi jumlah entri Activity Log tidak bertambah dibanding baseline

### TC-FA-CAID-247: Retroactive Mass Update tidak menulis log per aset

25. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
26. Pilih Separator `- (Dash)`
27. Klik `[Save]`
28. Tunggu aksi selesai: tombol `[Save]` kembali disabled
29. Buka Modal Changelog: Custom Asset ID
30. Verifikasi Changelog hanya memuat satu entri baru dibanding baseline (Edit Separator `Slash` ke `Dash`)
31. Verifikasi Changelog tidak memuat entri dengan Field `Asset ID` dari mass update
32. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
33. Verifikasi System Log hanya memuat satu entri baru dibanding baseline (Edit Separator `Slash` ke `Dash`)
34. Verifikasi System Log tidak memuat entri dengan Field `Asset ID` dari mass update
35. Buka Fixed Asset > Activity Log > tab User Action
36. Verifikasi Activity Log hanya memuat satu entri baru dibanding baseline (Edit Separator `Slash` ke `Dash`)
37. Verifikasi Activity Log tidak memuat entri dengan Field `Asset ID` dari mass update
38. Buka Fixed Asset > Assets > All Assets > Detail A1
39. Verifikasi Asset ID A1 menjadi `JKT-LAP-T490-0926-1`
40. Verifikasi tidak ada banner info per aset di Asset Detail

### TC-FA-CAID-252: Save yang ditolak tidak menulis entri log

41. Ganti akun: logout, lalu login sebagai Total Control `Company V07 65`
42. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
43. Centang `Division Code` lalu klik `[Save]`
44. Verifikasi alert inline V-07 `Asset ID would exceed 64 characters. Remove a segment or choose a shorter separator.` tampil
45. Buka Modal Changelog: Custom Asset ID
46. Verifikasi Changelog tidak memuat entri baru dibanding baseline
47. Tutup Modal Changelog: Custom Asset ID
48. Klik menu `Global Settings` pada sidebar navigasi
49. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning) tampil
50. Klik `[Leave]`
51. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
52. Verifikasi System Log tidak memuat entri baru dibanding baseline
53. Buka Fixed Asset > Activity Log > tab User Action
54. Verifikasi Activity Log tidak memuat entri baru dibanding baseline

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 54 langkah (ekspansi langkah 11 sampai 13 tiga kali menjadi 60), di atas smell 35 langkah. Alasan: seluruhnya satu kelas harness (kelas g, asersi absence log) dan tiap TC punya user dan baseline sendiri; blok baca-log berpola (buka surface, lalu `Verifikasi` jumlah atau kolom log) tidak dihitung menurut bagian 3 prinsip 13 (langkah 19 sampai 24, 29 sampai 37, 45 dan 46, serta 51 sampai 54), sehingga langkah di luar blok itu 33 (39 dengan ekspansi).
- Langkah 10 sampai 13 mengulang langkah 11 sampai 13 untuk A1, A2, A3 dengan parameter di tabel "Aset yang diperiksa" (bagian 8b butir 7).
- `P-5` butir (a): pemicu kelas lain hanya membentuk kondisi yang diasersi tidak tercatat: Save yang ditolak V-07 (TC-FA-CAID-252) dan Retroactive Mass Update (TC-FA-CAID-247) bukan objek uji; tiap TC memakai baseline sendiri.
- Anchor positif asersi absence (bagian 8b butir 2): header Detail aset yang menampilkan Asset ID aset pada langkah 12 (Expected TC-FA-CAID-72 c) sebagai anchor absence riwayat pada langkah 13, toast netral pada langkah 5 dan 17, entri Edit Separator baru pada langkah 30, 33, 36, alert V-07 pada langkah 44 (ditambahkan sebagai anchor penolakan, S-03), dan jumlah awal yang dicatat pada langkah 14, 25, dan 42. Langkah 39 (Asset ID A1 berubah) adalah anchor untuk absence banner pada langkah 40 dan didasarkan Expected TC-FA-CAID-247 ("walau Asset ID A1, A2, A3 berubah").
- Langkah penghubung: langkah 8, 14, 21, 23, 25, 29, 32, 35, 38, 42, 45, 51, dan 53 (membuka halaman), langkah 28 (tunggu aksi selesai sebelum membuka Modal Changelog, bagian 8b butir 8), langkah 41 (ganti akun), langkah 47 sampai 50 (menutup modal, lalu menutup form dirty lewat sidebar, `Verifikasi` dialog `Unsaved Changes`, dan `[Leave]`, S-08). Baseline pada langkah 14, 25, dan 42 mengikuti S-12; TC-FA-CAID-72 tidak mengasersi log sehingga tidak mencatat baseline.
- Seluruh TC memakai Company yang tidak diatur ulang di antara TC; TC-FA-CAID-246 dan TC-FA-CAID-247 memakai baseline jumlah entri terbaru sehingga tidak bergantung pada TC sebelumnya.
- Pembagian TC lintas spec: TC-FA-CAID-233 sampai 245 dan TC-FA-CAID-248 sampai 250 ada di spec 037 sampai 041. Absence atas request langsung yang ditolak dan state tenant ada di spec 098 (TC-FA-CAID-303 sampai 305), 099 (TC-FA-CAID-306 sampai 309, 337, dan 338), dan 100 (TC-FA-CAID-312 dan 313).
- Temuan untuk QA:
  - TC-FA-CAID-246 Expected b menyebut "Modified By/Last Updated konfigurasi" tanpa menyebut di surface mana kolom itu tampil; spec membandingkannya dengan nilai yang dicatat pada tab Custom Asset ID sebagai baseline.
  - TC-FA-CAID-252 menyebut pengguna Sarah Johnson pada `Company V07 65` yang dideskripsikan Pre-setup No 19 tanpa nama pengguna; identitas dan email akun `Company V07 65` ditulis "disediakan tim FE/BE".
  - TC-FA-CAID-247 Expected b memuat "tidak ada banner info per aset di Asset Detail" tanpa menyebut aset; spec memeriksa Detail A1.
  - Post Condition TC-FA-CAID-72, TC-FA-CAID-246, TC-FA-CAID-247, dan TC-FA-CAID-252 tidak diasersi karena TC tidak memberi langkah observasinya.
