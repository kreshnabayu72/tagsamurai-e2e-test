---
id: TC-GS-NLU-E2E-115-sinkronisasi-master-data-rename-position-division-dan-custom-field
title: "Sinkronisasi master data: rename Position Division dan Custom Field"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-420
  - TC-GS-NLU-421
  - TC-GS-NLU-422
  - TC-GS-NLU-423
coverage:
  web: automated
---

# Sinkronisasi master data: rename Position Division dan Custom Field

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- State global: spec ini mengubah nama master data dan Custom Field; semuanya data milik spec (bersuffix `{runId}-115`) yang dibuat hook `before` dan dihapus hook `after`, bukan data Pre-setup bersama. Suite berjalan serial (`parallel: false`).
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE):
  - Position `Field Technician {runId}-115` dan Division `Operations {runId}-115`.
  - Custom Field uji (aktif, tidak Required): `Blood Type Uji {runId}-115` (Dropdown, nilai A/B/O/AB), `Emergency Phone Uji {runId}-115` (Phone), `Badge Note Uji {runId}-115` (Text).
  - Non-Login User `Budi Kurniawan {runId}-115` (First Name `Budi`, Last Name `Kurniawan {runId}-115`, Position `Field Technician {runId}-115`, Division `Operations {runId}-115`, Email `budikurniawan+{runId}-115@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active) dengan nilai Custom Field: `Blood Type Uji {runId}-115` = `O`, `Emergency Phone Uji {runId}-115` = `081234567115`, `Badge Note Uji {runId}-115` = `Kartu A`.
- Nilai rename: Position menjadi `Lead Technician {runId}-115`, Division menjadi `Operations Hub {runId}-115`, Field Name menjadi `Blood Group Uji {runId}-115`, nilai Dropdown `O` menjadi `O+`.
- Pemulihan: hook `after` menghapus lewat API Non-Login User, Position, Division, dan Custom Field uji `{runId}-115` (nama apa pun yang sedang dipakai setelah rename), tanpa mengasumsikan seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-420: Rename Position dan Division tercermin di List dan Detail

1. Buka modul Position, rename Position `Field Technician {runId}-115` menjadi `Lead Technician {runId}-115`, lalu simpan
2. Buka modul Division, rename Division `Operations {runId}-115` menjadi `Operations Hub {runId}-115`, lalu simpan
3. Buka Global Settings > User > User List > sub-tab Non-Login User, ketik Search `Budi Kurniawan {runId}-115`, tekan Enter
4. Verifikasi sel Position baris `Budi Kurniawan {runId}-115` menampilkan `Lead Technician {runId}-115`
5. Verifikasi sel Division baris `Budi Kurniawan {runId}-115` menampilkan `Operations Hub {runId}-115`
6. Klik Name baris `Budi Kurniawan {runId}-115` untuk membuka Detail
7. Verifikasi Position pada Detail menampilkan `Lead Technician {runId}-115`
8. Verifikasi Division pada Detail menampilkan `Operations Hub {runId}-115`

### TC-GS-NLU-421: Custom Field rename Field Name dan rename nilai Dropdown tercermin di Detail

9. Buka modul Custom Field User, rename Field Name `Blood Type Uji {runId}-115` menjadi `Blood Group Uji {runId}-115`
10. Rename nilai Dropdown `O` menjadi `O+` pada field `Blood Group Uji {runId}-115`
11. Buka Detail Non-Login User `Budi Kurniawan {runId}-115` (sub-tab Non-Login User, Search `Budi Kurniawan {runId}-115`, klik Name baris)
12. Verifikasi label field `Blood Group Uji {runId}-115` tampil di Detail
13. Verifikasi nilai field `Blood Group Uji {runId}-115` menampilkan `O+` (nilai tersimpan tetap terhubung)

### TC-GS-NLU-422: Custom Field Deactivate menyembunyikan field dan nilai tanpa menghapus lalu Activate memulihkan

14. Buka modul Custom Field User dan nonaktifkan Custom Field `Badge Note Uji {runId}-115`
15. Buka Detail Non-Login User `Budi Kurniawan {runId}-115` (sub-tab Non-Login User, Search `Budi Kurniawan {runId}-115`, klik Name baris)
16. Verifikasi label field `Blood Group Uji {runId}-115` tampil di Detail
17. Verifikasi `Badge Note Uji {runId}-115` tidak tampil di Detail
18. Kembali ke list, klik `⋯` baris `Budi Kurniawan {runId}-115` > `Edit`
19. Verifikasi field `Blood Group Uji {runId}-115` tampil di Popup Edit
20. Verifikasi `Badge Note Uji {runId}-115` tidak tampil di Popup Edit
21. Tutup Popup Edit dengan `✕` (tanpa perubahan, tanpa dialog `Unsaved Changes`)
22. Buka modul Custom Field User dan aktifkan kembali Custom Field `Badge Note Uji {runId}-115`
23. Buka Detail Non-Login User `Budi Kurniawan {runId}-115` (sub-tab Non-Login User, Search `Budi Kurniawan {runId}-115`, klik Name baris)
24. Verifikasi nilai `Badge Note Uji {runId}-115` yang tersimpan (`Kartu A`) tampil lagi di Detail

### TC-GS-NLU-423: Custom Field Delete menghapus nilai dan Change Data Type mengosongkan nilai lama

25. Buka modul Custom Field User dan hapus Custom Field `Emergency Phone Uji {runId}-115`
26. Ubah Data Type `Badge Note Uji {runId}-115` dari Text ke Numeric, lalu konfirmasi
27. Buka Detail Non-Login User `Budi Kurniawan {runId}-115` (sub-tab Non-Login User, Search `Budi Kurniawan {runId}-115`, klik Name baris)
28. Verifikasi label field `Badge Note Uji {runId}-115` tampil di Detail
29. Verifikasi `Emergency Phone Uji {runId}-115` tidak tampil di Detail
30. Verifikasi nilai `Badge Note Uji {runId}-115` menjadi kosong `—`
31. Kembali ke list, klik `⋯` baris `Budi Kurniawan {runId}-115` > `Edit`
32. Verifikasi `Emergency Phone Uji {runId}-115` tidak tampil di Popup Edit
33. Tutup Popup Edit dengan `✕` (tanpa perubahan, tanpa dialog `Unsaved Changes`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 3, 11, 15, 23, 27 (membuka sub-tab dan Search record yang dicari), langkah 18, 31 (kembali ke list dan membuka Popup Edit), langkah 21, 33 (menutup Popup Edit yang tidak diubah, tanpa dialog `Unsaved Changes`), serta langkah 1, 9, 14, 22, 25 (aksi di modul Position, Division, dan Custom Field User sebagai pemicu).
- State global (R-08): nama Position, Division, dan Custom Field uji yang diubah adalah data milik spec; hook `after` menghapusnya sehingga Position `Driver`, `Manager` dan Custom Field dasar Pre-setup tidak berubah. Custom Field uji diberi suffix `{runId}-115` (S-12) walau daftar nama di `suite.md` tidak memuat suffix.
- Alasan jumlah langkah: nominal 33 langkah. Semua blok memakai satu record dan satu surface Detail yang sama, dan Detail dibuka berulang karena tiap TC mengubah state yang berbeda; kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap blok memakai field dan master data sendiri.
- Temuan untuk QA:
  - TC-GS-NLU-420 sampai 423 menyebut aksi "di modul masing-masing" (Position, Division, Custom Field User) tanpa merinci jalur menu, tombol, dan label dialog rename, Deactivate/Activate, Delete, dan Change Data Type; langkah ditulis generik tanpa label tombol yang tidak ada di TC.
  - TC-GS-NLU-420 dan 421 memakai Position, Division, dan Custom Field Pre-setup sebagai target rename; spec memakai master data dan field milik spec supaya rename tidak mengubah data bersama (S-06).
  - TC-GS-NLU-421 menyebut nilai Dropdown `O` dan nama field `Blood Type Uji`; nama field dan nilai di spec diberi suffix `{runId}-115` (S-12).
  - TC-GS-NLU-423 tidak menyebut nilai kolom curated pada List; spec hanya mengasersi Detail dan Popup Edit seperti Expected TC.
