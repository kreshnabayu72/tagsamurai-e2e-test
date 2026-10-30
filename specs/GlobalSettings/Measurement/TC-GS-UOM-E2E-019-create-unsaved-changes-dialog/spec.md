---
id: TC-GS-UOM-E2E-019-create-unsaved-changes-dialog
title: "Dialog Unsaved Changes pada Popup Create Unit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-58
  - TC-GS-UOM-59
  - TC-GS-UOM-60
  - TC-GS-UOM-61
  - TC-GS-UOM-62
coverage:
  web: automated
---

# Dialog Unsaved Changes pada Popup Create Unit

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji perilaku menutup popup Create Unit yang dirty.
- Hook suite (login akun default, `beforeEach` membuka Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`; pada run mock, API pendukung di luar modul (identitas pengguna, menu, flag Guided Tooltip) disediakan tim FE.
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).
- Kebutuhan mock (path endpoint mengikuti `openapi.yaml` dan `low-level-design.md` modul Measurement dan dilengkapi tim FE di skrip; tidak disalin di spec ini):
  - Sesi dan payload izin akun Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi) dengan capability Manage master reference lengkap. Login di hook `before` (env `GS_TC_PASSWORD` untuk run non-mock; tidak ditulis di spec).
  - Respons List Measurement: 8 unit Pre-setup Client A (Box, Dozen, Gram, Kilogram, Liter, Meter, Pack, Pieces), tanpa `Acre`.
  - Respons cek keunikan Unit Name (debounce sekitar 500 ms): nama tersedia untuk `Acre`, sehingga tidak ada error duplikat.
  - Endpoint Create Measurement tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal.
- Data: `Acre` dan Symbol `ac` hanya diketik dan tidak pernah tersimpan, sehingga tidak ada cleanup.
- Kemampuan teknis: penanganan dialog `beforeunload` bawaan browser (membaca bahwa dialog muncul lalu menolaknya agar tetap di halaman) untuk TC-GS-UOM-62; klik pada area backdrop di luar modal; penekanan Esc dan F5.
- State global: tidak ada yang diubah. Sesi tetap di akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.

## Test Steps

### TC-GS-UOM-60: Tombol Esc saat form Create dirty menampilkan dialog Unsaved Changes

1. Klik [+ Unit]
2. Ketik Symbol `ac`
3. Tekan Esc
4. Verifikasi dialog `Unsaved Changes` tampil
5. Verifikasi form belum tertutup
6. Klik [Cancel] pada dialog agar kembali ke form

### TC-GS-UOM-58: Close Create saat dirty lalu Cancel mempertahankan form

7. Ketik Unit Name `Acre`
8. Klik `[✕]`
9. Verifikasi dialog Title `Unsaved Changes` (warning), Body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` (severity warning)
10. Klik [Cancel]
11. Verifikasi dialog tertutup
12. Verifikasi form tetap terbuka
13. Verifikasi Unit Name `Acre` dipertahankan di form

### TC-GS-UOM-61: Klik backdrop saat form Create dirty tidak menutup form

14. Klik area backdrop di luar modal
15. Verifikasi form tetap terbuka
16. Verifikasi input Unit Name `Acre` dipertahankan
17. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-UOM-62: Reload tab saat form Create dirty memicu proteksi browser

18. Tekan F5
19. Verifikasi prompt konfirmasi browser keluar halaman (`beforeunload`) tampil sesuai `prd-conventions.md` §24.1d
20. Tolak reload pada prompt agar tetap berada di halaman dengan form Create terbuka

### TC-GS-UOM-59: Close Create saat dirty lalu Leave membuang input

21. Klik `[✕]`
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik [Leave]
24. Verifikasi dialog tertutup
25. Verifikasi modal tertutup
26. Verifikasi tabel menampilkan sedikitnya satu baris
27. Verifikasi `Acre` tidak ada di tabel

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec adalah 60, 58, 61, 62, 59 (urutan sumber 58 sampai 62). Alasan: hanya satu pembukaan form untuk lima TC; TC-GS-UOM-59 ([Leave]) menutup form dan membuang input sehingga ditaruh paling akhir (prinsip 6 konvensi). TC-GS-UOM-60 diletakkan pertama karena memakai Symbol `ac` yang ditambahkan Unit Name `Acre` oleh TC berikutnya; form tetap dirty sepanjang spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (menutup dialog dari TC-GS-UOM-60 dengan [Cancel] agar form tetap terbuka) dan langkah 20 (menolak reload agar form tetap terbuka). Langkah 22 memverifikasi dialog `Unsaved Changes` untuk menutup form dirty secara deterministik (S-08).
- Langkah 26 dan 27: `Acre` tidak ada di tabel (Expected Result b TC-GS-UOM-59); baris pembanding (langkah 26) mendahuluinya (butir 2 bagian 8b). Pada run mock asersi ini hanya membaca ulang respons mock List (butir "Readback respons mock") sehingga ditulis karena Expected Result TC memintanya.
- Rujukan data: Symbol `ac` (TC-GS-UOM-60) dan Unit Name `Acre` (TC-GS-UOM-58, 59, 61) hidup dalam form yang sama.
- Spec ini berdiri terpisah dari `TC-GS-UOM-E2E-018-create-screening-clear-field-dan-tutup-bersih` karena gabungan keduanya 59 langkah (32 + 27), jauh melewati batas 35 langkah; spec ini memakai satu form Create yang sengaja tetap dirty sepanjang spec dan membutuhkan penanganan dialog `beforeunload`, sedangkan 018 memakai form bersih dan form pasca-[Clear Field] tanpa kemampuan itu. Tiap spec membuka popup Create sendiri sehingga kegagalan satu spec tidak membuat spec lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-UOM-62 (`beforeunload`) memerlukan kemampuan menangani dialog bawaan browser (Prerequisites); bila tidak tersedia, TC ini tetap dicatat di sini dan tidak diganti langkah bersyarat.
  - Path dan skema endpoint mock disediakan tim FE sesuai `openapi.yaml` dan `low-level-design.md` modul (S-13).
