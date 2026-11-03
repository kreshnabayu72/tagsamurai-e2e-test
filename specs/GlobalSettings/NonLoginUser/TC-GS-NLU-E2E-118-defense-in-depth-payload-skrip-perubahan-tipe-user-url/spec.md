---
id: TC-GS-NLU-E2E-118-defense-in-depth-payload-skrip-perubahan-tipe-user-url
title: "Defense-in-depth: payload skrip, perubahan tipe user, URL Detail tidak valid, isolasi entitas"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-437
  - TC-GS-NLU-445
  - TC-GS-NLU-452
  - TC-GS-NLU-455
coverage:
  web: automated
---

# Defense-in-depth: payload skrip, perubahan tipe user, URL Detail tidak valid, isolasi entitas

## Prerequisites

- Mode: FE+BE. Create TC-GS-NLU-437 lewat UI di atas backend nyata; URL Detail dibuka langsung di browser; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE):
  - TC-GS-NLU-445: Non-Login User `Budi Tipe {runId}-118` (First Name `Budi`, Last Name `Tipe {runId}-118`, Division `Operations`, Email `budityipe+{runId}-118@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active).
  - TC-GS-NLU-452: tiga id Detail yang dibaca hook `before` lewat seeding: (1) id Non-Login User `Hapus Id {runId}-118` yang dibuat lalu dihapus, (2) id Login User `Ahmad Fauzi`, (3) id Non-Login User `Lintas Entitas {runId}-118` milik Client lain (Client lain dan akun pembuatnya disediakan tim FE/BE; lihat Temuan untuk QA).
  - TC-GS-NLU-455: Non-Login User `Entitas Lain Satu {runId}-118` di Client PT Sinar Abadi, bukan Client aktor (dibuat fixture BE; lihat Temuan untuk QA).
- Data yang dibuat TC-GS-NLU-437 lewat UI: First Name `<img src=x onerror=alert(1)>`, Last Name `Uji {runId}-118`, Email `xssuji+{runId}-118@qwertysystem.net`, Division `Logistics`, Represented By `Ahmad Fauzi`.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-118` yang tersisa (termasuk record dengan nama skrip dan data di Client lain).
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-437: Payload skrip pada nama tampil sebagai teks biasa di tabel dan Changelog

1. Klik `[+ Non-Login User]`
2. Isi First Name `<img src=x onerror=alert(1)>`, Last Name `Uji {runId}-118`, Email `xssuji+{runId}-118@qwertysystem.net`, Division `Logistics`
3. Pilih Represented By `Ahmad Fauzi` lewat popup Select User
4. Klik `[Submit]`
5. Tunggu aksi selesai (popup Create menutup)
6. Ketik Search `Uji {runId}-118`, tekan Enter
7. Verifikasi baris tabel menampilkan Name `<img src=x onerror=alert(1)> Uji {runId}-118` sebagai teks apa adanya
8. Verifikasi tidak ada dialog alert dan tidak ada skrip yang dijalankan pada tabel
9. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
10. Verifikasi entri `Create` pada Modal Changelog menampilkan New Value `<img src=x onerror=alert(1)> Uji {runId}-118` sebagai teks apa adanya
11. Verifikasi tidak ada dialog alert dan tidak ada skrip yang dijalankan pada Modal Changelog
12. Tutup Modal Changelog dengan `✕`

### TC-GS-NLU-445: Tipe user tidak dapat diubah lewat jalur selain Convert

13. Ketik Search `Budi Tipe {runId}-118`, tekan Enter, klik `⋯` baris `Budi Tipe {runId}-118` > `Edit`
14. Verifikasi Popup Edit memuat field First Name, Last Name, Position, Division, Employee ID, Email, dan Represented By
15. Verifikasi tidak ada field tipe user di Popup Edit
16. Tutup Popup Edit dengan `✕` (tanpa perubahan, tanpa dialog `Unsaved Changes`)
17. Klik `⋯` baris `Budi Tipe {runId}-118`
18. Verifikasi aksi `Convert to Login User` tersedia pada menu `⋯` sebagai jalan ke Login User
19. Tutup menu `⋯` dengan `Esc`

### TC-GS-NLU-452: URL Detail untuk id yang dihapus, bertipe Login User, atau milik entitas lain kembali ke List

20. Buka URL Detail dengan id Non-Login User `Hapus Id {runId}-118` yang sudah dihapus
21. Verifikasi toast netral `This non-login user is no longer available.`
22. Verifikasi halaman kembali ke List Non-Login User
23. Buka URL Detail dengan id Login User `Ahmad Fauzi`
24. Verifikasi toast netral `This non-login user is no longer available.`
25. Verifikasi halaman kembali ke List Non-Login User
26. Buka URL Detail dengan id Non-Login User `Lintas Entitas {runId}-118` milik Client lain
27. Verifikasi toast netral `This non-login user is no longer available.`
28. Verifikasi halaman kembali ke List Non-Login User
29. Verifikasi tidak ada data milik entitas lain (`Lintas Entitas {runId}-118`) yang tampil di halaman

### TC-GS-NLU-455: Non-Login User milik entitas lain tidak muncul di List maupun Search

30. Ketik Search `Entitas Lain Satu {runId}-118`, tekan Enter
31. Verifikasi empty state `No results found` tampil
32. Verifikasi tidak ada baris `Entitas Lain Satu {runId}-118` di tabel (data entitas lain tidak pernah tampil)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-GS-NLU-437 dan 445 adalah TC kelas a (defense-in-depth) yang tetap masuk spec FE+BE sebagai TC granular sumber (satu TC tepat satu spec).
- Langkah penghubung (S-03, R-16): langkah 5 (Tunggu aksi selesai), langkah 6, 13, 30 (Search record yang dicari), langkah 12, 16, 19 (menutup modal, popup, dan menu), langkah 1 (membuka popup Create).
- Asersi "tidak ada dialog alert" pada TC-GS-NLU-437 didahului `Verifikasi` baris atau entri yang sama tampil sebagai anchor (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-GS-NLU-445 Expected "satu-satunya jalan ke Login User adalah `Convert to Login User`" tidak dapat dibuktikan eksklusif lewat UI; spec mengasersi bahwa aksi itu tersedia di menu `⋯` dan bahwa Popup Edit tidak memuat field tipe user.
  - TC-GS-NLU-452 menyebut "id Non-Login User milik Client lain" tanpa menyebut Client lain atau akun yang membuat record; pola URL Detail dan cara mendapat id juga tidak disebut TC. Spec membaca id lewat seeding yang disediakan tim FE/BE.
  - TC-GS-NLU-455 menempatkan `Entitas Lain Satu` di Client PT Sinar Abadi (berstatus Suspended, Pre-setup No. 15) sehingga penulisan oleh seeding API ditolak guard Suspended; pembuatan data lewat fixture BE yang melewati guard itu disediakan tim FE/BE.
  - TC-GS-NLU-437 dan 445 tidak menyebut Post Condition yang punya langkah observasi.
