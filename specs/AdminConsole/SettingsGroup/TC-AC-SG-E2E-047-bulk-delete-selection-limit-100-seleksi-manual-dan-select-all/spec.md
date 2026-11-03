---
id: TC-AC-SG-E2E-047-bulk-delete-selection-limit-100-seleksi-manual-dan-select-all
title: "Bulk Delete: Selection Limit 100 pada Seleksi Manual dan Select All"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-169
  - TC-AC-SG-170
coverage:
  web: automated
---

# Bulk Delete: Selection Limit 100 pada Seleksi Manual dan Select All

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Seleksi Besar (Pre-setup #35) `totalControlSeleksi_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_SELEKSI_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #35 (entitas `Distributor Seleksi Besar`, volume 105 baris termasuk kelas e): 105 group level 1 bernama `Seleksi 001` sampai `Seleksi 105` tanpa entitas; N total = 105 (diturunkan dari seeding, bagian 8b butir 10).
- State global: Selection Limit = 100 (Pre-setup #34, System Limits di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits) untuk entitas ini. Hook `before` memastikan nilai 100 dan mencatat nilai awal lewat Fixture BE; hook `after` memulihkan nilai awal dan baseline entitas. Spec tidak mengubah nilai ini.
- Spec ini hanya memilih baris; tidak ada group yang dihapus atau diubah.
- Kemampuan teknis: Fixture BE (membaca dan menyetel Selection Limit entitas, pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-169: Seleksi manual ke-101 diblok oleh Selection Limit

1. Atur ukuran halaman tabel ke 100 baris
2. Untuk setiap baris pada halaman 1 (100 baris, `Seleksi 001` sampai `Seleksi 100` menurut urutan tabel), centang kolom Checkbox satu per satu
3. Verifikasi Bulk Actions Bar menampilkan "100 Groups selected"
4. Pindah ke halaman 2
5. Hover checkbox baris pertama pada halaman 2 (baris ke-101)
6. Verifikasi checkbox baris ke-101 disabled
7. Verifikasi tooltip "You've reached the maximum selection of 100 rows."
8. Verifikasi 100 seleksi sebelumnya tetap tercentang (Bulk Actions Bar tetap menampilkan "100 Groups selected")
9. Verifikasi tombol `Bulk Action` pada Bulk Actions Bar tetap bisa dipakai (enabled)
10. Klik ikon `×` pada Bulk Actions Bar

### TC-AC-SG-170: Select All di atas Selection Limit memilih 100 baris pertama dan menampilkan toast error

11. Pindah ke halaman 1
12. Centang kolom Checkbox pada baris pertama tabel
13. Klik "Select All (105 records)" pada Bulk Actions Bar
14. Verifikasi Bulk Actions Bar menampilkan "100 Groups selected"
15. Verifikasi toast error persisten tampil: "Error, only the first 100 of 105 rows were selected. Narrow your filter to include the rest."
16. Klik ikon `×` pada Bulk Actions Bar
17. Atur ukuran halaman tabel kembali ke 10 baris

## Notes

- Langkah 2 diulang untuk 100 baris (idiom "Untuk setiap baris", bagian 8b butir 7); parameter tiap iterasi adalah baris ke-1 sampai ke-100 halaman 1 dan tidak ada langkah bersyarat. Dengan ekspansi, spec ini sekitar 116 langkah eksekusi (di atas batas smell sekitar 35); alasan: semua blok satu kelas (e, volume data), TC-169 mensyaratkan 100 seleksi manual satu per satu, dan iterasi adalah satu aksi checkbox identik yang tidak dapat dikurangi tanpa mengubah TC.
- Langkah penghubung (S-03): langkah 1 dan 17 (ukuran halaman); langkah 10 dan 16 (membersihkan seleksi, S-09); langkah 11 dan 12 (kembali ke halaman 1 dan memilih satu baris agar Bulk Actions Bar tampil).
- Langkah 3 (`Verifikasi Bulk Actions Bar menampilkan "100 Groups selected"`) adalah asersi tambahan yang tidak ada di Expected TC-AC-SG-169: hitungan memastikan 100 seleksi manual benar-benar tercapai sebelum batas diuji pada baris ke-101, sehingga dipertahankan.
- Langkah 5 sampai 7 mengasersi state sementara (hover/tooltip) segera setelah hover (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-AC-SG-170 langkah 1 mengklik "Select All (105 records)" tanpa menyebut baris yang dicentang lebih dulu; spec memilih satu baris pertama agar Bulk Actions Bar tampil.
  - TC-AC-SG-169 "Bulk Actions Bar tetap bisa dipakai" tidak menyebut aksi; spec mengasersi tombol `Bulk Action` enabled.
  - Nilai Selection Limit 100 berasal dari Pre-setup #34; cara menyetelnya (akun dan layar System Limits) tidak tertulis di TC, sehingga ditulis sebagai kemampuan Fixture BE yang disediakan tim FE/BE.
