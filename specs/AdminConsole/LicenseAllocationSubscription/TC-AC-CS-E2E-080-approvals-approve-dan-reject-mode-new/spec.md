---
id: TC-AC-CS-E2E-080-approvals-approve-dan-reject-mode-new
title: "Approvals: Approve dan Reject Mode New"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-297
  - TC-AC-CS-298
  - TC-AC-CS-299
  - TC-AC-CS-310
coverage:
  web: automated
---

# Approvals: Approve dan Reject Mode New

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Eko Saputra, Total Control Distributor PT Maju Bersama (Pre-setup #9), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data seed milik spec (bersuffix `{runId}-080`, Plan Owner PT Maju Bersama (Distributor), requester Fajar Nugroho; dibuat di hook `before`, dihapus di hook `after`): pengajuan mode New `{idNew}` (Client `Apotek Sehat Sentosa+{runId}-080`, FAMS, plan Growth, Start Date `19/08/26`, Reserve $4,000.00, #49) untuk TC-AC-CS-297; pengajuan `{idFuture}` (Client `Toko Persetujuan+{runId}-080`, SAMS, plan Growth, Start Date `15/09/26`, Reserve $3,000.00, #124) untuk TC-AC-CS-298; pengajuan `{idRebase}` (Client `Toko Persetujuan Dua+{runId}-080`, FAMS, plan Growth, Start Date `18/08/26`, Duration 1 tahun, Reserve $4,000.00, #126) untuk TC-AC-CS-299 dengan approval dilakukan `19/08/26`; pengajuan `{idPrice}` (Client `Toko Persetujuan+{runId}-080`, FAMS, plan Professional, harga saat submit $10,000.00 per tahun, Reserve $10,000.00, lalu harga diubah fixture menjadi $12,000.00 sebelum approval, #124) untuk TC-AC-CS-310. Subscription ID `{idNew}`, `{idFuture}`, `{idRebase}`, dan `{idPrice}` dibaca lewat API seeding saat pengajuan dibuat dan dirujuk di langkah sebagai nilai terbaca (S-12). Pengajuan dibuat oleh requester lewat sesi API (Create-Only Distributor Fajar Nugroho, Pre-setup #6, `Spectra.env.AC_SUB_CREATE_PASSWORD`) hingga pengajuan tersimpan di hook `before`; approver login UI. General Settings Principal PT ABC (#28): Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00` (tidak diubah spec).
- Toggle `Require Approval for Allocation` untuk PT Maju Bersama ON (#23) dan Toggle `Require Approval for Trial Activation` (#24) diatur fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Kemampuan baca (disediakan tim FE/BE, tanpa endpoint karangan): saldo kantong Wallet (Reserve dan Capture), notifikasi per user untuk requester, dan Activation Email serta App Access per alamat.
- Jam: jam server dan jam browser diatur absolut lewat fixture waktu (tanggal acuan uji `19/08/26`), dan job sistem dipicu atau di-poll lewat kemampuan yang disediakan tim FE/BE (lihat suite.md). Jam dipulihkan di hook `after` dan sebelum membuka Changelog atau Subscription Log (S-09).
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state Pre-setup yang diubah spec dilakukan fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (suite.md; S-06 pengecualian 2026-10-30).
- Baseline: jumlah entri Changelog, Activity Log, dan System Log serta jumlah email dan notifikasi yang relevan dicatat sebelum aksi pemicu pertama lewat kemampuan baca yang disediakan tim FE/BE (hook `before`); asersi entri baru memakai selisih terhadap baseline atau pencarian Subscription ID (S-12, R-11). Date atau Last Updated diasersi dengan toleransi satu menit dan jam server serta jam browser sinkron.
- State global yang diubah: harga plan FAMS Professional (blok TC-AC-CS-310) dan jam server (blok TC-AC-CS-299), dipulihkan di hook `after` dan antar blok; keputusan Approve mengubah state pengajuan (dibersihkan fixture backend). Efeknya (Last Updated dan entri audit trail permanen) tidak memengaruhi asersi karena memakai Subscription ID.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-297: Approve term mode New dengan Start Date hari ini menjadi Active

1. Buka Approvals > Client Subscription, ketik Search `{idNew}`, tekan Enter, klik `[Review]` pada pengajuan `{idNew}`, pilih Approve, lalu klik Submit
2. Tunggu aksi selesai (dialog/modal tertutup)
3. Buka Allocation > Client Subscription tab "Current", ketik Search `{idNew}`, tekan Enter
4. Verifikasi term berstatus Active dengan Start Date `19/08/26`
5. Verifikasi approver dan waktu approval tercatat pada term
6. Verifikasi Wallet di-Capture $4,000.00 memakai harga snapshot saat submit
7. Buka modal Subscription Log term itu
8. Verifikasi Subscription Log memuat entri `Subscription approved by Eko Saputra`
9. Tutup modal, buka modal Changelog, ketik Search `{idNew}`, tekan Enter
10. Verifikasi sedikitnya satu entri lain milik term tampil di Changelog
11. Verifikasi Changelog tidak memuat Action `Approve`
12. Verifikasi requester menerima notifikasi "Subscription approved" dengan Body "{idNew} · FAMS · Apotek Sehat Sentosa+{runId}-080"
13. Verifikasi Activation Email dan App Access terkirim karena ini term pertama Client
14. Tutup modal Changelog dengan `✕`, lalu pulihkan baseline pengajuan lewat fixture backend

### TC-AC-CS-298: Approve term mode New dengan Start Date masa depan menjadi Pending

15. Buka Approvals > Client Subscription, ketik Search `{idFuture}`, tekan Enter, klik `[Review]` pada pengajuan `{idFuture}`, pilih Approve, isi Approval Note `Disetujui sesuai kontrak`, lalu klik Submit
16. Tunggu aksi selesai (dialog/modal tertutup)
17. Buka Allocation > Client Subscription tab "Current", ketik Search `{idFuture}`, tekan Enter
18. Verifikasi term berstatus Pending dengan Start Date sesuai pengajuan `15/09/26`
19. Verifikasi Reserve tetap ditahan tanpa Capture
20. Buka modal Subscription Log term itu
21. Verifikasi Subscription Log memuat entri `Subscription approved by Eko Saputra` dengan `Approval Note: Disetujui sesuai kontrak`
22. Tutup modal, buka modal Changelog, ketik Search `{idFuture}`, tekan Enter
23. Verifikasi sedikitnya satu entri lain milik term tampil di Changelog
24. Verifikasi Changelog tidak memuat Action `Approve`
25. Verifikasi Activation Email belum dikirim
26. Tutup modal Changelog dengan `✕`, lalu pulihkan baseline pengajuan lewat fixture backend

### TC-AC-CS-299: Approve mode New saat Start Date yang diinput sudah lewat melakukan rebase sekali

27. Atur jam server dan jam browser ke `19/08/26`, buka Approvals > Client Subscription, ketik Search `{idRebase}`, tekan Enter, klik `[Review]` pada pengajuan `{idRebase}`, pilih Approve, lalu klik Submit
28. Tunggu aksi selesai (dialog/modal tertutup)
29. Buka Allocation > Client Subscription tab "Current", ketik Search `{idRebase}`, tekan Enter, lalu klik baris untuk membuka Detail term
30. Verifikasi Start Date menjadi `19/08/26` dan End Date `18/08/27` (tanggal approval + 1 tahun - 1 hari)
31. Verifikasi term berstatus Active dan Capture $4,000.00 tanpa repricing
32. Verifikasi rebase hanya terjadi sekali
33. Verifikasi penyesuaian tanggal tidak menghasilkan notifikasi tersendiri dan requester hanya menerima notifikasi "Subscription approved"
34. Pulihkan baseline pengajuan lewat fixture backend

### TC-AC-CS-310: Approve memakai snapshot harga saat submit tanpa repricing

35. Buka Approvals > Client Subscription, ketik Search `{idPrice}`, tekan Enter, klik `[Review]` pada pengajuan `{idPrice}`, pilih Approve, lalu klik Submit
36. Tunggu aksi selesai (dialog/modal tertutup)
37. Buka Wallet dan Detail term `{idPrice}`
38. Verifikasi Capture sebesar $10,000.00 sesuai snapshot harga saat submit
39. Verifikasi tidak ada penghitungan ulang dengan harga $12,000.00
40. Pulihkan harga plan dan baseline pengajuan lewat fixture backend

## Notes

- Langkah penghubung: navigasi menu, Search (R-16: untuk menemukan baris target, termasuk Search di Approvals sebelum `[Review]`), `Tunggu aksi selesai` setelah tiap Approve (8b.8), penutupan modal, serta pemulihan jam, harga, dan baseline lewat fixture antar blok.
- P-1: asersi "modal Changelog tidak memuat Action `Approve`" (atau `Reject`) tetap di spec ini karena bergantung pada state berat (pengajuan ber-Reserve wallet yang diputuskan sekali dan tidak dapat diulang tanpa biaya besar); tiap asersi didahului Verifikasi entri lain milik term pada Changelog yang sama sebagai anchor positif dan memakai baseline jumlah entri (S-12). Approve dan Reject dicatat di Subscription Log, Activity Log, dan System Log approver (ACCS-LOGIC-06a).
- Alasan spec 40 langkah, di atas smell 35 langkah: keempat TC memakai akun approver yang sama, halaman Approvals yang sama, dan alur Approve atas pengajuan yang di-seed spec sendiri; tiap blok berdiri sendiri dengan baseline dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemecahan menambah hook, login, dan seeding tanpa menambah isolasi.
- Temuan untuk QA: (1) TC-AC-CS-297 menulis langkah approve sebagai "klik Submit" sedangkan TC Reject menulis `[Submit Decision]`; spec mengikuti teks TC. (2) TC-AC-CS-297 butir e dan TC-AC-CS-298 butir d (Activation Email) membutuhkan kemampuan baca email per alamat yang tidak disebut TC; disediakan tim FE/BE (R-11). (3) TC-AC-CS-297 Post Condition a dan b (baris pindah dari Waiting ke Active di List; pengajuan pindah ke Approvals Tab History dengan Decision Approved) tidak punya langkah observasi di Approvals sehingga tidak diasersi terpisah; baris Active di List ditutup oleh Verifikasi term Active. (4) TC-AC-CS-298 tidak menyebut approver dalam precondition `Eko Saputra` pada Subscription Log; spec memakai nama sesuai TC-AC-CS-297. (5) TC-AC-CS-299 butir d: "requester hanya menerima notifikasi Subscription approved" bersifat universal atas notifikasi; spec memakai kemampuan baca notifikasi requester. (6) TC-AC-CS-297, 298, 299, dan 310 tidak menyebut apakah Approvals > Client Subscription punya Search; spec memakai Search `{id}` sebelum `[Review]` (R-16) dan mengandalkan kemampuan itu ada (perlu dikonfirmasi QA). (7) Tanggal acuan `19/08/26` tidak ada sebagai precondition fixture waktu di TC-AC-CS-297 dan 299; spec memakai fixture waktu yang disediakan tim FE/BE.
