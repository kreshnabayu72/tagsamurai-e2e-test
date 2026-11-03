---
id: TC-GS-NLU-E2E-114-sinkronisasi-login-user-delete-mengosongkan-pointer-represented-by-dan-log
title: "Sinkronisasi Login User: Delete mengosongkan pointer Represented By, log Edit, dan pointer kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-415
  - TC-GS-NLU-416
  - TC-GS-NLU-417
coverage:
  web: automated
---

# Sinkronisasi Login User: Delete mengosongkan pointer Represented By, log Edit, dan pointer kosong

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Division `Operations`, Email `<nama>+{runId}-114@qwertysystem.net`):
  - TC-GS-NLU-415: Login User `Wawan Setiadi {runId}-114` (First Name `Wawan`, Last Name `Setiadi {runId}-114`, Active, Position `Manager`, Division `Warehouse`) dan Non-Login User `Eka Putri {runId}-114` dengan Represented By `Wawan Setiadi {runId}-114`.
  - TC-GS-NLU-416: Login User `Wakil Hapus {runId}-114` (First Name `Wakil`, Last Name `Hapus {runId}-114`, Active) dan Non-Login User `Log Pointer {runId}-114` dengan Represented By `Wakil Hapus {runId}-114`. Login User itu dihapus oleh Siti Nurhaliza lewat UI di dalam spec (langkah 11 dan sesudahnya).
  - TC-GS-NLU-417: Non-Login User `Pointer Kosong {runId}-114` (First Name `Pointer`, Last Name `Kosong {runId}-114`) dengan Represented By kosong akibat Delete Login User `Wakil Kosong {runId}-114`; hook `before` membuat Login User itu, mengaitkannya ke `Pointer Kosong`, lalu menghapusnya lewat API.
- Baseline log TC-GS-NLU-416: jumlah entri Activity Log dan System Log aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` dicatat sebelum Delete Login User `Wakil Hapus`; kemampuan membaca jumlah entri disediakan tim FE/BE.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-114` yang tersisa (Login User dan Non-Login User).
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-415: Delete Login User yang menjadi Represented By mengosongkan pointer di List dan Detail

1. Buka sub-tab Login User lewat Global Settings > User > User List, ketik Search `Setiadi {runId}-114`, tekan Enter, klik `⋯` baris `Wawan Setiadi {runId}-114` > `Delete`
2. Klik `[Delete]` pada dialog konfirmasi
3. Tunggu aksi selesai (dialog Delete menutup)
4. Buka sub-tab Non-Login User, ketik Search `Eka Putri {runId}-114`, tekan Enter
5. Verifikasi sel Represented By baris `Eka Putri {runId}-114` menampilkan `—` tanpa link
6. Klik Name baris `Eka Putri {runId}-114` untuk membuka Detail
7. Verifikasi Detail menampilkan Represented By `—`

### TC-GS-NLU-416: Delete Login User menulis log Edit Represented By ke tiga surface atas nama admin penghapus

8. Buka Global Settings > Activity Log lewat sidebar dan catat jumlah entri aktor Siti Nurhaliza untuk object Non-Login User per Action `Edit` sebagai baseline Activity Log
9. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User) dan catat jumlah entri per Action `Edit` sebagai baseline System Log aktor
10. Buka sub-tab Login User, ketik Search `Hapus {runId}-114`, tekan Enter, klik `⋯` baris `Wakil Hapus {runId}-114` > `Delete`
11. Klik `[Delete]` pada dialog konfirmasi
12. Tunggu aksi selesai (dialog Delete menutup)
13. Ketik Search `Log Pointer {runId}-114`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
14. Verifikasi Tab Changelog Detail: entri `Edit` Field `Represented By`, Old Value `Wakil Hapus {runId}-114`, New Value `—`, Modified By `Siti N` (admin yang menghapus)
15. Buka Global Settings > Activity Log lewat sidebar
16. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
17. Verifikasi Activity Log: entri baru memuat Action `Edit`, object Non-Login User, dan aktor Siti Nurhaliza, sama dengan entri di Changelog
18. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
19. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
20. Verifikasi System Log aktor: entri baru memuat Action `Edit`, object Non-Login User, dan aktor Siti Nurhaliza, sama dengan entri di Changelog
21. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-417: Edit Non-Login User dengan pointer kosong mewajibkan memilih Login User aktif baru

22. Ketik Search `Pointer Kosong {runId}-114`, tekan Enter, klik `⋯` baris `Pointer Kosong {runId}-114` > `Edit`
23. Ubah First Name menjadi `Pointerx` tanpa memilih Represented By, lalu klik `[Save]`
24. Verifikasi field Represented By menampilkan `[+ Select User]`
25. Verifikasi pesan inline `Represented by must not be empty` dan penyimpanan ditolak
26. Pilih Represented By `Ahmad Fauzi` lewat popup Select User, lalu klik `[Save]`
27. Verifikasi Toast sukses `Success, non-login user has been updated.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 4, 10, 22 (membuka sub-tab dan Search record yang dicari), langkah 3 dan 12 (Tunggu aksi selesai), serta navigasi sidebar dan klik Name di blok baca-log.
- Baseline (S-12): TC-GS-NLU-416 mencatat jumlah entri Activity Log dan System Log aktor per Action `Edit` sebelum Delete `Wakil Hapus`, lalu tiap asersi memakai selisih; Changelog memakai nama record bersuffix `{runId}-114`.
- Langkah baca-log berpola dan baseline tidak dihitung menurut Smell bagian 3 prinsip 13: nominal 27 langkah, 11 langkah blok baca-log, 16 langkah terhitung.
- Login User pada TC-GS-NLU-415, 416, dan 417 adalah akun milik spec (bukan Login User Pre-setup `Wawan Setiadi` dan `Wakil Hapus`) supaya Delete tidak mengubah data bersama (S-06). Delete Login User `Wakil Hapus` dilakukan di dalam spec oleh Siti Nurhaliza sehingga Modified By entri adalah admin penghapus.
- Temuan untuk QA:
  - TC-GS-NLU-416 memuat Login User `Wakil Hapus` yang "sudah dihapus oleh Siti Nurhaliza" sebagai precondition tanpa langkah Delete; spec menjalankan Delete itu di dalam spec supaya log dan Modified By dapat diasersi.
  - Tab `System Log` dan Activity Log tidak dirinci jalur navigasinya di TC (lihat spec 108); spec memakai baseline jumlah entri per Action dan aktor.
  - Expected TC-GS-NLU-417 a menggabungkan tampilan `[+ Select User]` dan penolakan simpan; spec mengasersinya sesudah `[Save]` pertama (R-03).
