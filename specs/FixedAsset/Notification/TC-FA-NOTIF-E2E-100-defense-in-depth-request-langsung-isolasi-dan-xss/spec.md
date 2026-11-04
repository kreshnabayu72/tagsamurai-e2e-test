---
id: TC-FA-NOTIF-E2E-100-defense-in-depth-request-langsung-isolasi-dan-xss
title: "Defense-in-Depth: Request Langsung ke Server, Isolasi Kepemilikan Notifikasi, dan Payload XSS"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-NOTIF-352
  - TC-FA-NOTIF-353
  - TC-FA-NOTIF-355
  - TC-FA-NOTIF-357
  - TC-FA-NOTIF-358
  - TC-FA-NOTIF-400
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung ke Server, Isolasi Kepemilikan Notifikasi, dan Payload XSS

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`. Akun ini juga memegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pendukung:
  - Approver (Borrowing & Assignment) Gedung A (Pre-setup #4), `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERBA_PASSWORD`, `Fixture.fixedAssetNotification.approverBorrowingAssignment`; hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`) sebagai pelaku yang menindak transaksi.
  - Asset Admin (Pre-setup #8), `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`; sesi API aktor sebagai pembuat Borrow Request dan sesi UI (login pada langkah 31) sebagai pemohon.
  - Staff (Pre-setup #9), `staffDisposal_automated_{namaCompany}@qwertysystem.net`; tidak login, hanya sebagai pemilik notifikasi yang dibaca lewat fixture BE. TC tidak menyebut akun Staff mana yang dimaksud (lihat Temuan untuk QA).
- Data Pre-setup: notifikasi N-01 sampai N-07 (Pre-setup #17; N-01 sampai N-05 Unread, N-06 dan N-07 Read, badge `5`; N-01 actionable; N-07 actionable dengan task TASK-Q3-A Completed), transaksi Borrow BRW-2026-0341 (2 aset) dan BRW-2026-0342 (1 aset Kamera DSLR AST-2024-0141) (Pre-setup #19 dan #24). Spec mengubah status BRW-2026-0341 (langkah 22) dan BRW-2026-0342 (langkah 28 dan 29); fixture BE pemulih seed notifikasi dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before`, di langkah 26, dan di hook `after`. Satu notifikasi milik Staff tersedia (dibaca lewat fixture BE; identitasnya dicatat di langkah 6).
- Pengecualian S-06/S-12 butir A-16: notifikasi seed N-01 sampai N-07 (Pre-setup #17) dan transaksi BRW-2026-0341 serta BRW-2026-0342 (Pre-setup #19 sampai #24) dipakai literal tanpa suffix `{runId}-100` sebagai target Mark as Read, Approve, dan Reject, karena ID transaksi dibangkitkan sistem, ditulis literal di Expected TC, dan notifikasi seed hanya ada untuk akun Pre-setup. Pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (langkah 26); suite berjalan serial (`parallel: false`).
- Nilai Rejection Reason uji keamanan: `<b>x</b><script>alert(1)</script>` (`Fixture.fixedAssetNotification.xssRejectionReason`).
- Kemampuan teknis: klien HTTP untuk request langsung ke server memakai sesi Total Control; fixture BE untuk membaca status notifikasi dan jumlah Unread (badge) tanpa melalui browser; sesi API aktor; fixture BE pemicu event modul sumber (Submit, Approve, Reject Borrow). Semuanya disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Env var `FA_TC_PASSWORD`, `FA_APPROVERBA_PASSWORD`, dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` menyetelnya dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-352: Server menolak Mark as Read pada notifikasi actionable Unread

1. Kirim request Mark as Read langsung ke server untuk N-01 tanpa melalui UI, memakai sesi Total Control, hingga respons diterima
2. Verifikasi respons berstatus `422`
3. Verifikasi pesan respons `"Cannot mark task-oriented notification as read directly."`
4. Periksa status N-01 lewat fixture BE
5. Verifikasi status N-01 tetap Unread

### TC-FA-NOTIF-353: Server menolak Mark as Read pada notifikasi milik user lain

6. Catat identitas dan status satu notifikasi milik Staff lewat fixture BE (baseline)
7. Kirim request Mark as Read langsung ke server untuk notifikasi milik Staff tersebut memakai sesi Total Control, hingga respons diterima
8. Verifikasi respons berstatus `403`
9. Periksa status notifikasi Staff lewat fixture BE
10. Verifikasi status notifikasi Staff sama dengan baseline langkah 6 (tidak berubah)

### TC-FA-NOTIF-355: Snapshot dan list hanya memuat notifikasi milik user yang login

11. Minta snapshot dan list notifikasi langsung ke server memakai sesi Total Control, hingga respons diterima
12. Verifikasi respons memuat notifikasi N-01 sampai N-07 milik Total Control (anchor positif)
13. Verifikasi seluruh notifikasi pada respons milik Total Control
14. Bandingkan dengan notifikasi Staff dari langkah 6: Verifikasi respons tidak memuat notifikasi milik Staff

### TC-FA-NOTIF-400: Mark as Read langsung pada notifikasi actionable yang sudah Read

15. Kirim request Mark as Read langsung ke server untuk N-07 tanpa melalui UI, memakai sesi Total Control, hingga respons diterima
16. Verifikasi respons berstatus `200 OK` (No-Op, bukan `422`)
17. Periksa status N-07 dan jumlah Unread (badge Bell icon) lewat fixture BE
18. Verifikasi status N-07 tetap Read
19. Verifikasi jumlah Unread (badge Bell icon) tetap `5`

### TC-FA-NOTIF-358: Defense-in-depth, Approve langsung divalidasi ulang modul pemilik

20. Klik Bell icon
21. Klik `[Detail]` pada item N-01
22. Dari akun Approver (Borrowing & Assignment, Pre-setup #4, sesi API), Approve BRW-2026-0341 hingga status akhir tersimpan
23. Tunggu aksi selesai
24. Kirim request Approve BRW-2026-0341 langsung ke server memakai sesi Total Control, hingga respons diterima
25. Verifikasi server menolak Approve (respons penolakan, bukan sukses)

### TC-FA-NOTIF-357: Payload teks Rejection Reason dirender sebagai teks, bukan HTML

26. Pulihkan seed notifikasi dan transaksi Pre-setup #17 sampai #24 lewat fixture BE pemulih
27. Tunggu aksi selesai
28. Dari akun Asset Admin (Pre-setup #8, sesi API), Submit Borrow Request BRW-2026-0342 hingga status Waiting for Approval tersimpan
29. Dari akun Approver (Pre-setup #4, sesi API), Reject BRW-2026-0342 dengan Rejection Reason `<b>x</b><script>alert(1)</script>` hingga status Rejected tersimpan
30. Tunggu aksi selesai
31. Logout, lalu login sebagai Asset Admin pemohon (Pre-setup #8) dengan `Spectra.env.FA_ASSETADMIN_PASSWORD`, lalu buka Fixed Asset > Dashboard
32. Klik Bell icon
33. Verifikasi Body item `"BRW-2026-0342: <b>x</b><script>alert(1)</script>"` tampil sebagai teks literal
34. Verifikasi tidak ada script yang berjalan (tidak ada dialog `alert` pada browser)

## Notes

- Pengecualian `K-1` (bagian 2 konvensi): TC-FA-NOTIF-352, 353, 355, 358, dan 400 adalah TC kelas a (defense-in-depth) dengan Expected berupa respons API; tetap masuk spec FE+BE walau tumpang tindih dengan `tc-notification-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec. Asersi pada langkah request langsung hanya status respons dan state data lewat fixture BE (bagian 8b butir 1); tampilan Bell icon tidak diasersi pada langkah-langkah itu.
- Langkah penghubung (S-03): langkah 6 (baseline status notifikasi Staff, S-12); langkah 20 dan 21 (membuka halaman Approvals dari N-01 sesuai langkah 1 TC-FA-NOTIF-358; halaman tujuan tidak diasersi karena Expected TC hanya penolakan Approve); langkah 22 (pelaku kedua lewat sesi API); langkah 23, 27, dan 30 (tunggu aksi selesai, bagian 8b butir 8); langkah 26 (pemulihan seed antar TC); langkah 28 dan 29 (pemicu Submit dan Reject lewat sesi API); langkah 31 (ganti akun eksplisit, S-07).
- Urutan blok: TC yang tidak mengubah data (352, 353, 355, 400) lebih dulu, lalu TC-FA-NOTIF-358 yang mengubah BRW-2026-0341, dan TC-FA-NOTIF-357 terakhir karena memerlukan pemulihan seed, pemicu Submit dan Reject, dan ganti akun ke pemohon; dengan urutan ini state hasil blok yang mengubah data tidak mengganggu blok read-only (S-10).
- TC-FA-NOTIF-358: pada langkah 22 transaksi BRW-2026-0341 sudah ditindak pihak lain (Approver, sesi API) sebelum request langsung langkah 24; langkah 21 membuka halaman Approvals dari N-01.
- Seed Pre-setup #17 (N-01 sampai N-07) juga dipakai spec kelas lain (multi-konteks); pemisahan mengikuti satu spec satu kelas harness (kelas a defense-in-depth di sini).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 14 didahului langkah 12 (notifikasi milik Total Control tampil pada respons yang sama); langkah 34 didahului langkah 33 (item tampil sebagai teks literal pada Dropdown Panel yang sama).
- Pada TC-FA-NOTIF-358 yang diasersi hanya "server menolak Approve"; kode status penolakan dan hasil penolakan dirujuk ke TC modul `approvals/` dan tidak diasersi ulang, sesuai Expected TC.
- Pada TC-FA-NOTIF-357 kolom Expected menulis "tidak ada script berjalan"; diasersi sebagai tidak adanya dialog `alert` browser (langkah 34) karena TC tidak menyebut cara pengamatannya.
- Temuan untuk QA:
  - TC-FA-NOTIF-353: "notifikasi milik Staff" tanpa nomor Pre-setup; akun Staff diambil dari satu-satunya role Staff pada tabel Pre-setup (#9, Staff Disposal), dan identitas notifikasi Staff tidak ditulis di Data Uji.
  - TC-FA-NOTIF-355: "bandingkan dengan notifikasi Staff" tanpa identitas notifikasi Staff; memakai notifikasi dari langkah 6.
  - TC-FA-NOTIF-357: "pemohon BRW-2026-0342" tidak disebut akunnya (Pre-setup #19 tidak menulis pembuat); TC-FA-NOTIF-418 menulis Asset Admin sebagai PIC pembuat BRW-2026-0342 sehingga spec memakai Asset Admin Pre-setup #8. Precondition TC login sebagai Total Control, sedangkan langkah mengamati Bell icon sebagai pemohon.
  - TC-FA-NOTIF-358: Expected merujuk hasil penolakan ke TC modul `approvals/` tanpa asersi (kode status tidak tertulis).
  - TC-FA-NOTIF-352, 353, 355, 358, dan 400: Post Condition kosong (`-`) atau tanpa langkah observasi; tidak diasersi.
  - TC-FA-NOTIF-400: badge diperiksa lewat fixture BE (sesuai langkah 2 TC), bukan tampilan Bell icon.
