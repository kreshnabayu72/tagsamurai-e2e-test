---
id: TC-AC-SG-E2E-044-bulk-delete-homogen-campuran-dan-seluruh-baris-punya-member
title: "Bulk Delete: Homogen Tanpa Entitas, Campuran dengan Skip Member, dan Seluruh Baris Punya Member"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-157
  - TC-AC-SG-158
  - TC-AC-SG-159
coverage:
  web: automated
---

# Bulk Delete: Homogen Tanpa Entitas, Campuran dengan Skip Member, dan Seluruh Baris Punya Member

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Hapus Utama (Pre-setup #21) `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #21 (entitas `Distributor Hapus Utama`), nama literal karena TC mengasersi nama baris pada dialog:
  - `Hapus Bulk 1` dan `Hapus Bulk 2` (tanpa entitas): dihapus pada TC-157.
  - `Hapus Campur 1` dan `Hapus Campur 2` (tanpa entitas): dihapus pada TC-158.
  - `Hapus Campur M1` dan `Hapus Campur M2` (masing-masing satu Client Active; nama Client tidak tertulis di Pre-setup): TC-158 men-skip M1, TC-159 memilih M1 dan M2 dan diblok.
- Spec ini menghapus node Pre-setup `Hapus Bulk 1`, `Hapus Bulk 2`, `Hapus Campur 1`, dan `Hapus Campur 2` (TC mengasersi nama dan komposisi Pre-setup, S-06 pengecualian 2026-10-30). Pemulihan lewat Fixture BE di hook `before` dan `after`; TC-159 (diblok) berada paling awal dan hanya membaca. Efek: Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) entitas bertambah oleh penghapusan dan pemulihan dan tidak diasersi.
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-159: Bulk Delete seluruh baris punya member diblok (D-09)

1. Ketik Search `Hapus Campur M`, tekan Enter
2. Centang kolom Checkbox pada baris `Hapus Campur M1` dan `Hapus Campur M2`
3. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
4. Verifikasi dialog blok tampil: title "Cannot Delete Groups", body bullet `Hapus Campur M1` dan `Hapus Campur M2` serta "These groups or their subgroups still have members. Remove all members before deleting." dengan satu tombol `[OK]`
5. Klik `[OK]`
6. Verifikasi tidak ada toast sukses
7. Verifikasi seleksi dan Bulk Actions Bar dipertahankan ("2 Groups selected")
8. Klik ikon `×` pada Bulk Actions Bar

### TC-AC-SG-157: Bulk Delete homogen dua group tanpa entitas (D-06)

9. Ganti isi kotak search dengan `Hapus Bulk`, tekan Enter
10. Centang kolom Checkbox pada baris `Hapus Bulk 1` dan `Hapus Bulk 2`
11. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
12. Verifikasi dialog tampil: title "Delete Groups", body bullet `Hapus Bulk 1` dan `Hapus Bulk 2` serta "Are you sure you want to delete them? This action cannot be undone." dengan `[Cancel]` dan `[Delete]`
13. Klik `[Delete]` pada dialog
14. Verifikasi toast sukses: "Success, group has been deleted."
15. Verifikasi `Hapus Bulk 1` dan `Hapus Bulk 2` hilang dari tabel
16. Verifikasi Bulk Actions Bar hilang
17. Verifikasi seleksi direset ke 0

### TC-AC-SG-158: Bulk Delete campuran: sebagian diproses dan sebagian di-skip karena member (D-07)

18. Ganti isi kotak search dengan `Hapus Campur`, tekan Enter
19. Centang kolom Checkbox pada baris `Hapus Campur 1`, `Hapus Campur 2`, dan `Hapus Campur M1`
20. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
21. Verifikasi dialog tampil: title "Delete Groups"; kelompok bullet "The following will be deleted:" (`Hapus Campur 1`, `Hapus Campur 2`) dan "The following have members and will be skipped:" (`Hapus Campur M1`); penutup "Are you sure you want to continue? This action cannot be undone." dengan `[Cancel]` dan `[Continue]`
22. Klik `[Continue]`
23. Verifikasi toast: "Success, group has been deleted. Some items were skipped (still has members)."
24. Verifikasi `Hapus Campur M1` tetap ada
25. Verifikasi seleksi direset ke 0

## Notes

- Langkah penghubung (S-03): langkah 1, 9, dan 18 (Search untuk menemukan baris target, R-16); langkah 5 (`[OK]` menutup dialog blok); langkah 8 (membersihkan seleksi, S-09).
- Perubahan urutan TC (S-10): TC-159 (diblok) ditempatkan paling awal, sebelum TC-157 dan TC-158 yang benar-benar menghapus data.
- Langkah 6 (tidak ada toast sukses) diletakkan segera setelah `[OK]`; anchor positif adalah dialog blok pada langkah 4 (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-AC-SG-159 butir a menyebut "bukan D-08" tanpa mendefinisikan teks pembeda selain judul "Cannot Delete Groups" dan body member; spec mengasersi judul dan body.
  - Nama Client pada `Hapus Campur M1` dan `Hapus Campur M2` tidak tertulis di Pre-setup #21.
