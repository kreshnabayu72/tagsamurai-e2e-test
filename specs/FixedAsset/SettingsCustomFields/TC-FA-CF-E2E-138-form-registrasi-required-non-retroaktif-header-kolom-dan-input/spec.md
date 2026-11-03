---
id: TC-FA-CF-E2E-138-form-registrasi-required-non-retroaktif-header-kolom-dan-input
title: "Form Aset: Required Non-Retroaktif, Header Kolom Opsional, dan Kontrol Input"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-538
  - TC-FA-CF-539
  - TC-FA-CF-544
  - TC-FA-CF-657
  - TC-FA-CF-658
coverage:
  web: automated
---

# Form Aset: Required Non-Retroaktif, Header Kolom Opsional, dan Kontrol Input

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Nilai (Pre-setup #1 dan #18). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun kedua (ganti akun eksplisit pada langkah 13): Total Control Company Alpha, pengguna Sarah Johnson (Pre-setup #1) dengan `Spectra.env.FA_TC_PASSWORD`; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Company Nilai (Pre-setup #18; dasar Company Alpha #11 dan baseline #12) dengan aset A1 (Pump, Active), A2 (Generator, Active), dan A3 (Pump, deleted), dirujuk lewat fixture `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE). Field yang diubah: `Required Check` (Text, Required No, tanpa nilai), `Required Hello` (Text, Required No, `Hello` pada A1), dan `Maintenance Note` (Text, General, `Checked` pada A1). TC-FA-CF-544 dan 657 memakai Company Alpha (Pre-setup #11 dan #12; aset konsumen A1 dan A2, Pre-setup #31) dengan `Asset Serial Tag` (Active) dan `Depreciated Ratio` (Inactive); hasil rename `Serial Number {runId}-138`.
- Kemampuan teknis (disediakan tim FE): preferensi kolom Asset List yang mungkin tersimpan di browser dihapus oleh hook `after`; spec hanya membuka dan menutup Column Visibility tanpa menyimpan.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-538: Perubahan Required tidak berlaku surut

1. Klik row action `⋯` > `Edit` pada baris `Required Check`, ubah Required menjadi Yes, lalu klik `[Save]`
2. Buka Edit aset `A2` (belum bernilai `Required Check`) dan simpan tanpa mengubah field itu
3. Verifikasi aset `A2` tersimpan
4. Verifikasi tidak ada error validasi pada input `Required Check` (aset lama tidak divalidasi mundur)

### TC-FA-CF-539: Validasi Required dijalankan pada Edit aset berikutnya hanya bila nilai field diubah atau dikosongkan

5. Buka Fixed Asset > Settings > Custom Fields, klik row action `⋯` > `Edit` pada baris `Required Hello`, ubah Required menjadi Yes, lalu klik `[Save]`
6. Buka Edit aset `A1` (bernilai `Hello`), kosongkan nilai `Required Hello`, lalu simpan
7. Verifikasi penyimpanan ditolak dengan pesan inline pada input `Required Hello` (teks pesan tidak diassert)
8. Isi kembali input `Required Hello` dengan `Hello` (nilai tersimpan) lalu tutup form edit aset dengan `✕`

### TC-FA-CF-658: Mengganti Data Type menyesuaikan kontrol input pada form registrasi aset

9. Buka Fixed Asset > Settings > Custom Fields, klik row action `⋯` > `Edit` pada baris `Maintenance Note`, ganti Data Type menjadi `Date`, klik `[Save]`, lalu klik `[Change Data Type]` pada dialog
10. Buka form registrasi aset pada modul Asset Registration untuk Asset Name `Pump`
11. Verifikasi input `Maintenance Note` berupa kontrol tanggal dengan placeholder `Select date`
12. Tutup form registrasi aset (form belum diisi, sehingga tanpa dialog `Unsaved Changes`)

### TC-FA-CF-544: Asset List menampilkan kolom opsional custom field aktif pada Column Visibility

13. Ganti akun: logout, lalu login sebagai Total Control Company Alpha (Pre-setup #1)
14. Buka Asset List dan klik header kolom Actions (⋯)
15. Verifikasi daftar kolom opsional memuat custom field Active `Asset Serial Tag`
16. Verifikasi daftar kolom opsional tidak memuat custom field Inactive `Depreciated Ratio`
17. Tutup Column Visibility tanpa menyimpan

### TC-FA-CF-657: Rename Field Name tercermin pada header kolom opsional tabel aset

18. Buka Fixed Asset > Settings > Custom Fields, klik row action `⋯` > `Edit` pada baris `Asset Serial Tag`, ubah Field Name menjadi `Serial Number {runId}-138`, lalu klik `[Save]`
19. Buka Asset List dan klik header kolom Actions (⋯)
20. Verifikasi daftar kolom opsional memuat `Serial Number {runId}-138`
21. Verifikasi daftar kolom opsional tidak memuat `Asset Serial Tag`
22. Tutup Column Visibility tanpa menyimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec memuat TC lintas modul (NC-01): form registrasi aset, Edit aset, dan Asset List tidak didefinisikan PRD modul ini; spec hanya mengasersi sejauh teks Expected TC.
- Urutan TC di spec: 538, 539, 658 (Company Nilai), lalu 544 dan 657 (Company Alpha). Ganti akun eksplisit pada langkah 13 karena TC-FA-CF-544 dan TC-FA-CF-657 mensyaratkan Company Alpha; TC-FA-CF-657 mengganti nama field sehingga berjalan sesudah TC-FA-CF-544 (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13, menutup form edit dan form registrasi, serta menutup Column Visibility. Langkah "Isi kembali input `Required Hello` ... " memulihkan form dirty (S-09, dicatat di sini).
- Temuan untuk QA:
  - TC-FA-CF-538 dan TC-FA-CF-539 tidak menyebut tombol simpan form edit aset; spec menulis "simpan".
  - TC-FA-CF-658 "untuk Asset Name apa pun" tidak menentukan Asset Name; spec memakai `Pump`.
  - TC-FA-CF-544 dan TC-FA-CF-657 tidak menyebut tombol penutup Column Visibility; spec menulis "Tutup Column Visibility tanpa menyimpan".
  - Email akun Total Control Company Nilai tidak tertulis di Pre-setup TC; env var `FA_TC_NILAI_PASSWORD` disediakan tim FE.
