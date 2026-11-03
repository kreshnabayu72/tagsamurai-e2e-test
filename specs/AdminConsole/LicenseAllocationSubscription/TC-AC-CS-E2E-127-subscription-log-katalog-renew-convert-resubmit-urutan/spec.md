---
id: TC-AC-CS-E2E-127-subscription-log-katalog-renew-convert-resubmit-urutan
title: "Subscription Log: Katalog Renew, Convert, Resubmit, Urutan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-606
  - TC-AC-CS-607
  - TC-AC-CS-608
coverage:
  web: automated
---

# Subscription Log: Katalog Renew, Convert, Resubmit, Urutan

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun pemicu lewat sesi API (bukan sesi UI), dijalankan di hook `before` spec ini:

| Pre-setup | Email | Peran | Env password |
|---|---|---|---|
| #1 | akun aktor UI di atas (`Hendra Wijaya`) | Total Control Principal | `Spectra.env.AC_SUB_TC_PASSWORD` |
| #5 | `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`) | Group Manager Distributor, bypass approval | `Spectra.env.AC_SUB_GM_PASSWORD` |

- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-127`). Tidak ada baris Pre-setup bersama yang ditulis spec ini; entri Changelog dan Subscription Log yang terbentuk bersifat permanen. Subscription ID yang dibentuk sistem dibaca lewat API seeding:
  1. Client `Bengkel Maju Jaya+{runId}-127` dengan term SAMS Expired `{idBengkel}` (setara `SUBS-20250819-00002`).
  2. Client `Warung Kopi Senja+{runId}-127` dengan term FAMS Active `{idWarung}` (setara `SUBS-20250815-00001`).
  3. Client `Klinik Harapan Bunda+{runId}-127` dengan trial SAMS Growth Active.
- Aksi pemicu hook `before` (berurutan, hingga tersimpan; endpoint tulis tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim FE/BE, lihat Temuan untuk QA). Jumlah entri `{idBengkel}` dicatat sebagai baseline sebelum pemicu pertama (S-12):
  1. TC-AC-CS-606: `Hendra Wijaya` me-Renew `{idBengkel}` Client `Bengkel Maju Jaya+{runId}-127` SAMS (Expired) dengan Keep current plan, Duration `1` (efek langsung), dan menjadwalkan Renew `{idWarung}` Client `Warung Kopi Senja+{runId}-127` FAMS ke plan Professional (efektif `01/09/26`).
  2. TC-AC-CS-607: `Dewi Anggraini` meng-Convert trial Client `Klinik Harapan Bunda+{runId}-127` SAMS Growth ke plan Professional lewat bypass.
- Data Pre-setup baca-saja (tidak ditulis spec): `SUBS-20260813-00001` (#55: Client Optik Cahaya, FAMS, Growth, Waiting for Approval, Plan Owner CV Karya Mandiri, hasil Resubmit oleh `Rina Pratama` dari `SUBS-20260805-00001`), `SUBS-20260805-00001` (#56: Canceled oleh Timeout Auto-Cancel); Subscription Log keduanya sudah tercatat saat fixture dibuat.
- Seed dan efek pemicu dibersihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu), dipulihkan di hook `after`; End Date `18/08/27` dan tanggal efektif Renew diturunkan dari tanggal acuan itu.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-606: Entri Subscription renewed dan Renewal scheduled pada Renew efek langsung dan terjadwal

1. Ketik Search `Bengkel Maju Jaya+{runId}-127`, tekan Enter
2. Klik ikon `⋯` pada term Active hasil Renew `Bengkel Maju Jaya+{runId}-127` SAMS, klik `Subscription Log`
3. Verifikasi modal memuat entri `Subscription renewed by Hendra Wijaya` dengan baris Description `Plan: Growth` dan `End Date: 18/08/27`
4. Verifikasi tidak ada entri `Subscription created` pada term itu
5. Klik `[✕]`
6. Ganti isi kotak search dengan `Warung Kopi Senja+{runId}-127`, tekan Enter
7. Klik ikon `⋯` pada predecessor `{idWarung}`, klik `Subscription Log`
8. Verifikasi entri `Renewal scheduled by Hendra Wijaya` dengan `Pending Renewal: Professional, effective 01/09/26`
9. Verifikasi header `Status:` badge Active
10. Verifikasi tidak ada entri `Subscription renewed`
11. Klik `[✕]`
12. Klik tab `History`
13. Ganti isi kotak search dengan `{idBengkel}`, tekan Enter
14. Klik ikon `⋯` pada predecessor `{idBengkel}`, klik `Subscription Log`
15. Verifikasi header `Status:` badge Renewed
16. Verifikasi jumlah entri Subscription Log `{idBengkel}` sama dengan baseline sebelum pemicu
17. Klik `[✕]`

### TC-AC-CS-607: Entri Subscription converted tercatat pada record Trial

18. Ganti isi kotak search dengan `Klinik Harapan Bunda+{runId}-127`, tekan Enter
19. Klik ikon `⋯` pada baris Trial `Klinik Harapan Bunda+{runId}-127` SAMS yang Converted, klik `Subscription Log`
20. Verifikasi entri teratas `Subscription converted by Dewi Anggraini` dengan baris Description `New Plan: Professional (Paid)`
21. Verifikasi di bawahnya entri `Subscription created` dari aktivasi trial
22. Verifikasi header `Status:` badge Converted
23. Klik `[✕]`
24. Klik tab `Current`
25. Ganti isi kotak search dengan `Klinik Harapan Bunda+{runId}-127`, tekan Enter
26. Klik ikon `⋯` pada term paid hasil Convert `Klinik Harapan Bunda+{runId}-127` SAMS, klik `Subscription Log`
27. Verifikasi modal memuat entri pembuatan `Subscription created by Dewi Anggraini`
28. Verifikasi tidak ada entri `Subscription approved` maupun `Subscription converted` pada term paid
29. Klik `[✕]`

### TC-AC-CS-608: Resubmit membuat Subscription Log baru dengan Resubmitted From dan log asal tidak berubah

30. Ganti isi kotak search dengan `SUBS-20260813-00001`, tekan Enter
31. Klik ikon `⋯` pada baris `SUBS-20260813-00001`, klik `Subscription Log`
32. Verifikasi entri `Subscription created by Rina Pratama` dengan baris Description `Type`, `Plan`, `Duration`, dan `Resubmitted From: SUBS-20260805-00001`
33. Klik `[✕]`
34. Klik tab `History`
35. Ganti isi kotak search dengan `SUBS-20260805-00001`, tekan Enter
36. Klik ikon `⋯` pada baris `SUBS-20260805-00001`, klik `Subscription Log`
37. Verifikasi modal `SUBS-20260805-00001` hanya memuat entri `Subscription created` dan `Subscription auto-canceled` (`Reason: Approval timeout`), tanpa entri baru akibat Resubmit
38. Verifikasi Subscription ID pada header modal ini `SUBS-20260805-00001`, berbeda dari modal `SUBS-20260813-00001` sehingga kedua record punya Subscription Log sendiri

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-609 (urutan, immutability, dan Edit No-Op) ada di spec 156.
- Aksi pemicu dijalankan di hook `before` (S-04, seeding API); pelaku kedua lewat sesi API bukan konteks kedua (`P-2` tidak dipakai).
- Langkah penghubung (S-03): langkah 1, 6, 13, 18, 25, 30, 35 (Search untuk menemukan baris target, R-16), langkah 5, 11, 17, 23, 29, 33 (menutup modal), dan langkah 12, 24, 34 (pindah tab).
- Spec ini melewati ~35 langkah (38). Alasan: satu topik (katalog entri Subscription Log berdasarkan jenis kejadian) dan satu permukaan, tiap blok membaca log record seeded berbeda sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pemecahan hanya menambah login dan hook.
- TC-AC-CS-606 Expected c dan TC-AC-CS-607 Expected d ("tidak ada entri ...") ditulis sebagai asersi state pada modal dengan anchor entri yang tampil di modal yang sama, bukan kelas g.
- Temuan untuk QA:
  - TC-AC-CS-606 Expected d ("tanpa entri baru dari Renew ini") tidak memberi cara mengetahui jumlah entri awal; spec memakai baseline jumlah entri yang dibaca sebelum pemicu (kemampuan baca disediakan tim FE/BE).
  - TC-AC-CS-606 menyebut dua aksi Renew (efek langsung dan terjadwal) tetapi satu langkah Dependensi per aksi tidak menyebut jam/tanggal; tanggal efektif `01/09/26` diambil dari Expected.
  - TC-AC-CS-607 langkah 1 menyebut baris Trial `Klinik Harapan Bunda` SAMS tanpa Subscription ID.
  - Aksi pemicu pada kolom Dependensi TC (TC-AC-CS-148, 149, 243) tidak punya endpoint tulis di TC, PRD, atau LLD (S-13).
