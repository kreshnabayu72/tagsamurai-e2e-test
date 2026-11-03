---
id: TC-AC-LA-E2E-123-log-create-principal-dan-event-created
title: "Log Create oleh Principal: New Value Free dan Event Allocation created"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-384
  - TC-AC-LA-518
coverage:
  web: automated
---

# Log Create oleh Principal: New Value Free dan Event Allocation created

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Hendra Wijaya; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Hendra Wijaya | #1 | Total Control Principal | `totalControlLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), Require Approval for Allocation OFF (Pre-setup #39).
- Data Dinamis: alokasi dikenali lewat Allocation ID unik hasil Submit (`{idFree3}`, `{idFree4}`); entri log milik ID itu berbaseline nol (S-12).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk jam server dan jam browser dengan nilai absolut; pemulihan baseline alokasi milik spec ini di hook `after`.
- State global: jam server dan jam browser diatur ke `22 Dec 2026` pada blok TC-AC-LA-518 dan dipulihkan setelah Submit; hook `after` memulihkan jam sebagai cadangan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Log Create oleh Principal pada tiga surface (TC-AC-LA-384)

1. Klik `[+ Allocation]`
2. Pilih Client `PT Sejahtera`
3. Pilih Target `SUBS-20260101-A1B2C`
4. Pilih Type `Concurrent User`
5. Isi Additional Quantity `3`
6. Klik `[Submit]`
7. Catat Allocation ID baris baru sebagai `{idFree3}`
8. Klik ikon `Changelog` pada List
9. Ketik Search `{idFree3}`, tekan Enter
10. Verifikasi Changelog memuat entri dengan Field `Allocation Details`, Old `—`, New `Concurrent User +3 to PT Sejahtera` tanpa teks `Paid via wallet`
11. Tutup modal Changelog
12. Buka Detail User `Hendra Wijaya` > tab System Log
13. Ketik Search `{idFree3}`, tekan Enter
14. Verifikasi System Log aktor memuat entri dengan Field `Allocation Details`, Old `—`, New `Concurrent User +3 to PT Sejahtera` tanpa teks `Paid via wallet`
15. Buka Activity Log Admin Console
16. Ketik Search `{idFree3}`, tekan Enter
17. Verifikasi Activity Log memuat entri dengan Field `Allocation Details`, Old `—`, New `Concurrent User +3 to PT Sejahtera` tanpa teks `Paid via wallet`
18. Verifikasi Modified By pada entri Activity Log adalah `Hendra W`
19. Buka Allocation > License Allocation (tab Current)

### Event Allocation created oleh Principal: Cost Free dan Paid From (TC-AC-LA-518)

20. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
21. Klik `[+ Allocation]`
22. Pilih Client `PT Sejahtera`
23. Pilih Target `SUBS-20260101-A1B2C`
24. Pilih Type `Concurrent User`
25. Isi Additional Quantity `4`
26. Klik `[Submit]`
27. Catat Allocation ID baris baru sebagai `{idFree4}`
28. Pulihkan jam server dan jam browser ke waktu nyata
29. Ketik Search `{idFree4}`, tekan Enter
30. Klik row action `Allocation Log` pada baris `{idFree4}`
31. Verifikasi entri Allocation Log berjudul `Allocation created by Hendra W`
32. Verifikasi Description entri memuat `Product: FAMS`, `License Type: Concurrent User`, `Target: SUBS-20260101-A1B2C`, `Quantity: +4`, `Cost: Free`
33. Verifikasi header modal `Paid From:` menampilkan `—`
34. Verifikasi tidak ada baris `Resubmitted From` pada entri
35. Tutup modal Allocation Log

## Notes

- Langkah penghubung (S-03, R-16): langkah 9, 13, 16, dan 29 (Search entri atau baris berdasarkan Allocation ID), langkah 11 dan 35 (menutup modal), langkah 19 (kembali ke List), langkah 20 dan 28 (mengatur dan memulihkan jam).
- Langkah 34 adalah asersi absence atas satu baris pada modal yang sudah terbuka dan memuat entri `{idFree4}`; langkah 31 sampai 33 pada modal yang sama menjadi anchor positifnya.
- Temuan untuk QA:
  - TC-AC-LA-384 tidak menyebut cara menemukan entri di tiga surface maupun akun System Log aktor; spec memakai Detail User `Hendra Wijaya` dan Search dengan Allocation ID unik.
  - TC-AC-LA-518 butir b menyebut header modal `Paid From:` bernilai `—` tanpa menyatakan bahwa header itu bagian dari modal Allocation Log yang sama dengan entri; spec membaca header pada modal yang sama.
  - TC-AC-LA-518 menyebut tanggal acuan 22 Dec 2026 meski Cost Free tidak bergantung tanggal; spec tetap mengikuti TC.
