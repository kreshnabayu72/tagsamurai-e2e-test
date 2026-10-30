---
id: TC-GS-UCF-E2E-035-edit-decimal-places-terkunci
title: "Edit Custom Field Numeric: Decimal Places Bebas pada Field Belum Bernilai, Terkunci Setelah Ada Nilai User, Clear Field, dan Pemulihan Decimal Places Tersimpan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-100
  - TC-GS-UCF-367
  - TC-GS-UCF-101
  - TC-GS-UCF-109
  - TC-GS-UCF-461
coverage:
  web: automated
---

# Edit Custom Field Numeric: Decimal Places Bebas pada Field Belum Bernilai, Terkunci Setelah Ada Nilai User, Clear Field, dan Pemulihan Decimal Places Tersimpan

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun aktor (login di hook `before`; password hanya lewat env var): Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`.
- Layar awal Global Settings > User > Custom Field dibuka hook `beforeEach`; `## Test Steps` tidak mengulang langkah buka.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup tidak dipakai.
- Data Dinamis milik spec (seeding lewat API di hook `before`, bersuffix `{runId}-035`; fixture baru `Fixture.customFieldUser.edit035`; Active, Required No, Placeholder kosong kecuali dinyatakan lain):
  - `Dec Free {runId}-035`: Numeric, Decimal Places 2, belum pernah memiliki nilai User (TC-GS-UCF-100).
  - `Dec Locked {runId}-035`: Numeric, Decimal Places 1, nilai User Rahmat Hidayat = `12.5` (TC-GS-UCF-367 dan 101; dipakai sebagai precondition TC, nilai User di-seed lewat mekanisme yang disediakan tim FE/BE).
  - `Dt Probe Ever {runId}-035`: Text; pernah bernilai lalu dikosongkan lewat ganti Data Type, tanpa nilai User saat ini (TC-GS-UCF-109; keadaan "pernah bernilai" di-seed lewat mekanisme yang disediakan tim FE/BE, TC tidak mendefinisikan caranya).
  - `Dec Round Trip {runId}-035`: Numeric, Decimal Places 1, nilai User Rahmat Hidayat = `7.5` (TC-GS-UCF-461).
- Akun Login User Client A `rahmatHidayat_automated_qaTeam1@qwertysystem.net` (Rahmat Hidayat) hanya menjadi pemilik nilai Custom Field yang dibaca pada Detail User (TC-GS-UCF-461).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-035` (menghapus pula nilai User terkait).
- Kemampuan teknis: tidak ada di luar sesi browser biasa.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Persiapan tabel

1. Ketik Search `{runId}-035`, tekan Enter

### TC-GS-UCF-367: Clear Field pada Edit field Numeric terkunci mengosongkan Data Type dan memulihkan Decimal Places tersimpan saat Numeric dipilih kembali

2. Klik `⋯` pada baris `Dec Locked {runId}-035`, pilih `Edit`
3. Klik `[Clear Field]`
4. Verifikasi Field Name kosong
5. Verifikasi Data Type kosong
6. Verifikasi Placeholder kosong
7. Verifikasi Decimal Places tidak tampil
8. Verifikasi Required kembali No
9. Pilih Data Type `Numeric`
10. Verifikasi Decimal Places tampil dengan nilai tersimpan `1`, bukan `0`
11. Klik `[✕]`
12. Verifikasi dialog `Unsaved Changes` tampil (form dirty karena nilai berbeda dari nilai tersimpan)
13. Klik `[Leave]`
14. Verifikasi `Dec Locked {runId}-035` tidak berubah (Value Setting `1 Decimal Place`)

### TC-GS-UCF-101: Decimal Places terkunci setelah ada nilai User, memilih nilai berbeda menampilkan dialog dan nilai kembali

15. Klik `⋯` pada baris `Dec Locked {runId}-035`, pilih `Edit`
16. Verifikasi pilihan Decimal Places Enabled
17. Verifikasi pilihan Decimal Places bernilai `1`
18. Pilih Decimal Places `2`
19. Verifikasi dialog `Decimal Places Locked`: `This field's decimal places is locked because it's already used by users. Delete this field and create a new one to change it.` dengan tombol `[OK]`
20. Klik `[OK]`
21. Verifikasi nilai Decimal Places kembali `1`
22. Ubah Placeholder menjadi `x`, klik `[Save]`
23. Verifikasi toast sukses: "Success, custom field has been updated."
24. Verifikasi Placeholder `x` tersimpan pada baris `Dec Locked {runId}-035`
25. Verifikasi Decimal Places tetap `1` (Value Setting `1 Decimal Place`)

### TC-GS-UCF-100: Decimal Places field Numeric yang belum pernah bernilai dapat diubah bebas

26. Klik `⋯` pada baris `Dec Free {runId}-035`, pilih `Edit`
27. Pilih Decimal Places `0`
28. Klik `[Save]`
29. Verifikasi toast sukses: "Success, custom field has been updated."
30. Verifikasi Value Setting baris `Dec Free {runId}-035` menampilkan `0 Decimal Places`
31. Klik `⋯` pada baris `Dec Free {runId}-035`, pilih `Edit`
32. Pilih Decimal Places `1`
33. Klik `[Save]`
34. Verifikasi Value Setting baris `Dec Free {runId}-035` menampilkan `1 Decimal Place`

### TC-GS-UCF-109: Decimal Places setelah Data Type diubah ke Numeric pada field yang pernah bernilai

35. Klik `⋯` pada baris `Dt Probe Ever {runId}-035`, pilih `Edit`
36. Ubah Data Type menjadi `Numeric`
37. Verifikasi Decimal Places tampil dengan nilai awal `0`
38. Verifikasi Decimal Places Enabled dan bebas dipilih (nilai lama sudah dikosongkan)
39. Pilih Decimal Places `2`, klik `[Save]`
40. Verifikasi toast sukses: "Success, custom field has been updated."
41. Verifikasi Value Setting baris `Dt Probe Ever {runId}-035` menampilkan `2 Decimal Places`
42. Klik `⋯` pada baris `Dt Probe Ever {runId}-035`, pilih `Edit`
43. Verifikasi Decimal Places tampil dengan nilai `2`
44. Verifikasi Decimal Places Enabled
45. Pilih Decimal Places `1`
46. Verifikasi dialog `Decimal Places Locked`: `This field's decimal places is locked because it's already used by users. Delete this field and create a new one to change it.` dengan tombol `[OK]`
47. Klik `[OK]`
48. Verifikasi nilai Decimal Places kembali `2`
49. Klik `[✕]`

### TC-GS-UCF-461: Kembali memilih Data Type Numeric tersimpan memulihkan Decimal Places tersimpan beserta kunci

50. Ganti isi kotak search dengan `Dec Round Trip {runId}-035`, tekan Enter
51. Klik `⋯` pada baris `Dec Round Trip {runId}-035`, pilih `Edit`
52. Ubah Data Type menjadi `Text`
53. Verifikasi Decimal Places tidak tampil
54. Pilih kembali Data Type `Numeric`
55. Verifikasi Decimal Places tampil dengan nilai tersimpan `1` (bukan `0`)
56. Pilih Decimal Places `2`
57. Verifikasi dialog `Decimal Places Locked`: `This field's decimal places is locked because it's already used by users. Delete this field and create a new one to change it.` dengan tombol `[OK]`
58. Klik `[OK]`
59. Verifikasi nilai Decimal Places kembali `1`
60. Klik `[Save]`
61. Verifikasi toast netral (Info): "No changes to save."
62. Verifikasi dialog `Change Data Type` tidak tampil
63. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
64. Verifikasi Detail User Rahmat Hidayat menampilkan nilai `7.5` pada `Dec Round Trip {runId}-035`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 64 langkah (di atas smell sekitar 35 langkah): seluruhnya satu kelas (fungsional, Decimal Places pada popup Edit), satu akun, dan tiap blok memakai field seed sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; jumlah langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected.
- Urutan TC: TC-GS-UCF-367 (tanpa Save) mendahului TC-GS-UCF-101 yang menyimpan Placeholder `x` pada field yang sama (`Dec Locked`); TC-GS-UCF-100, 109, dan 461 berurutan sesudahnya. Urutan berbeda dari TC sumber (100, 101, 109, 461, 367).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target dan menutup popup `✕` tanpa dialog (akhir TC-GS-UCF-109, popup tidak dirty karena dialog mengembalikan nilai).
- Pembagian TC lintas spec: TC-GS-UCF-102 dan 540 (Decimal Places pada form stale) ada di spec 038.
- Temuan untuk QA:
  - TC-GS-UCF-109: Precondition "pernah bernilai lalu dikosongkan lewat ganti Data Type" (D-30) tidak punya cara seeding di TC; disediakan tim FE/BE.
  - TC-GS-UCF-109: Expected d menulis "Setelah langkah 5 pada Edit berikutnya": nomor langkah merujuk langkah TC; spec memetakan ke urutan Edit kedua.
  - TC-GS-UCF-461: keadaan popup (tertutup atau tetap terbuka) sesudah toast netral tidak dinyatakan TC; spec langsung berpindah ke Detail User.
  - Keputusan NC-10 (teks `0 Decimal Places`, `1 Decimal Place`, `2 Decimal Places`), NC-19 (dialog `Decimal Places Locked` untuk 409), dan NC-22 (Text → Numeric bebas Decimal Places) berbeda dari API/LLD; asersi mengikuti TC dan backend nyata dapat gagal sampai LLD diselaraskan.
