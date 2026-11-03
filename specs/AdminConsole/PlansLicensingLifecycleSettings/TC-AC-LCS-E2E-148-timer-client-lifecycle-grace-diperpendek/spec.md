---
id: TC-AC-LCS-E2E-148-timer-client-lifecycle-grace-diperpendek
title: "Recalculation Timer Client Lifecycle: Grace Period Duration Diperpendek dan Batas Hari ke-14 dan ke-15"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-519
  - TC-AC-LCS-520
  - TC-AC-LCS-521
  - TC-AC-LCS-522
  - TC-AC-LCS-523
coverage:
  web: automated
---

# Recalculation Timer Client Lifecycle: Grace Period Duration Diperpendek dan Batas Hari ke-14 dan ke-15

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: subscription PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`) berstatus `Grace` pada hari masa tenggang yang diatur per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC). Hari dihitung sebagai hari kalender UTC dan job lifecycle berjalan satu kali sehari pada 00:00 UTC.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default.
- Waktu: tanggal data uji diatur lewat Fixture BE; jam server tidak digeser kecuali disebut pada langkah. Jam yang dimajukan dipulihkan lewat Fixture BE sesudah tiap TC dan di hook `after` suite (S-09); suite berjalan serial (`parallel: false`) karena spec ini memakai state global (jam, job, konfigurasi tab).
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-519: Grace Period Duration diperpendek: langganan yang masih dalam batas baru tetap Grace

1. Atur lewat Fixture BE: subscription PT Maju Jaya berstatus `Grace` pada hari ke-10 masa tenggang (Grace Period Duration `30`)
2. Klik tab `Client Lifecycle`
3. Ubah Grace Period Duration dari `30` menjadi `15`
4. Klik `[Save]` dan tunggu toast sukses
5. Picu eksekusi job lifecycle lewat Fixture BE
6. Buka Allocation > Client Subscription > List Subscriptions
7. Verifikasi status subscription PT Maju Jaya tetap `Grace` (sisa masa tenggang mengikuti durasi baru)

### TC-AC-LCS-520: Grace Period Duration diperpendek hingga timer terlewati: transisi ke Archive pada eksekusi job berikutnya

8. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription PT Maju Jaya berstatus `Grace` pada hari ke-20 masa tenggang (Grace Period Duration `30`)
9. Klik tab `Client Lifecycle`
10. Ubah Grace Period Duration dari `30` menjadi `15`
11. Klik `[Save]` dan tunggu toast sukses
12. Verifikasi toast sukses "Success, client lifecycle settings have been saved." tampil segera tanpa menunggu job
13. Picu eksekusi job lifecycle lewat Fixture BE
14. Buka Allocation > Client Subscription > List Subscriptions
15. Verifikasi status subscription PT Maju Jaya `Archive`

### TC-AC-LCS-521: Dua fase terlewati sekaligus: satu fase per eksekusi job

16. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription PT Maju Jaya berstatus `Grace` pada hari ke-20 masa tenggang dengan nilai tersimpan Archive Period Duration `30`, Purge Warning Email `10`, dan Purge Urgent Warning Email `2`
17. Klik tab `Client Lifecycle`
18. Ubah Grace Period Duration menjadi `15`, Archive Period Duration menjadi `2`, Purge Warning Email menjadi `2`, dan Purge Urgent Warning Email menjadi `1`
19. Klik `[Save]` dan tunggu toast sukses
20. Picu eksekusi job lifecycle pertama lewat Fixture BE
21. Buka Allocation > Client Subscription > List Subscriptions
22. Verifikasi status subscription PT Maju Jaya `Archive` (bukan `Purge` dan bukan `Deleted`)
23. Picu eksekusi job lifecycle kedua lewat Fixture BE
24. Muat ulang halaman List Subscriptions
25. Verifikasi status subscription PT Maju Jaya `Purge`

### TC-AC-LCS-522: Grace Period Duration diperpendek: langganan tepat pada hari ke-15 masa tenggang bertransisi ke Archive

26. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription PT Maju Jaya berstatus `Grace` pada hari ke-15 masa tenggang tepat (hari dihitung sebagai hari kalender UTC dan job lifecycle berjalan satu kali sehari pada 00:00 UTC)
27. Klik tab `Client Lifecycle`
28. Ubah Grace Period Duration dari `30` menjadi `15`
29. Klik `[Save]` dan tunggu toast sukses
30. Picu eksekusi job lifecycle lewat Fixture BE
31. Buka Allocation > Client Subscription > List Subscriptions
32. Verifikasi status subscription PT Maju Jaya `Archive` (batas yang tercapai pada hari ke-15 dianggap terlewati)

### TC-AC-LCS-523: Grace Period Duration diperpendek: langganan pada hari ke-14 masa tenggang tetap Grace

33. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription PT Maju Jaya berstatus `Grace` pada hari ke-14 masa tenggang (hari dihitung sebagai hari kalender UTC dan job lifecycle berjalan satu kali sehari pada 00:00 UTC)
34. Klik tab `Client Lifecycle`
35. Ubah Grace Period Duration dari `30` menjadi `15`
36. Klik `[Save]` dan tunggu toast sukses
37. Picu eksekusi job lifecycle lewat Fixture BE
38. Buka Allocation > Client Subscription > List Subscriptions
39. Verifikasi status subscription PT Maju Jaya tetap `Grace` (batas 15 hari belum tercapai)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Klik tab", "Picu eksekusi job ...", "Muat ulang halaman List Subscriptions", dan "Pulihkan ..." antar TC (S-03, S-09).
- Alasan lebih dari sekitar 35 langkah: lima blok memakai pola yang sama (state subscription diseed, Grace Period Duration diubah, job dipicu, status dibaca), semuanya satu kelas harness yang sama, dan tiap blok diseed ulang sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-AC-LCS-520 menulis "Amati status sebelum job berikutnya berjalan" dan Expected "toast sukses tampil segera"; spec mengasersi toast sebelum job dipicu dan tidak menambah asersi status sebelum job (S-02). Mekanisme memicu job lifecycle dan mengatur hari masa tenggang tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
