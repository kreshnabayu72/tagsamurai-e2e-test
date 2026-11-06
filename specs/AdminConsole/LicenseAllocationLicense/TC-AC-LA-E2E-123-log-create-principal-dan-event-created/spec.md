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

1. Catat baseline Allocation ID baris di halaman pertama tab Current
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`
4. Pilih Target `SUBS-20260101-A1B2C`
5. Pilih Type `Concurrent User`
6. Isi Additional Quantity `3`
7. Klik `[Submit]`
8. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idFree3}`
9. Klik ikon `Changelog` pada List
10. Ketik Search `{idFree3}`, tekan Enter
11. Verifikasi Changelog memuat entri dengan Field `Allocation Details`, Old `—`, New `Concurrent User +3 to PT Sejahtera` tanpa teks `Paid via wallet`
12. Tutup modal Changelog
13. Buka Detail User `Hendra Wijaya` > tab System Log
14. Ketik Search `{idFree3}`, tekan Enter
15. Verifikasi System Log aktor memuat entri dengan Field `Allocation Details`, Old `—`, New `Concurrent User +3 to PT Sejahtera` tanpa teks `Paid via wallet`
16. Buka Activity Log Admin Console
17. Ketik Search `{idFree3}`, tekan Enter
18. Verifikasi Activity Log memuat entri dengan Field `Allocation Details`, Old `—`, New `Concurrent User +3 to PT Sejahtera` tanpa teks `Paid via wallet`
19. Verifikasi Modified By pada entri Activity Log adalah `Hendra W`
20. Buka Allocation > License Allocation (tab Current)

### Event Allocation created oleh Principal: Cost Free dan Paid From (TC-AC-LA-518)

21. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
22. Catat baseline Allocation ID baris di halaman pertama tab Current
23. Klik `[+ Allocation]`
24. Pilih Client `PT Sejahtera`
25. Pilih Target `SUBS-20260101-A1B2C`
26. Pilih Type `Concurrent User`
27. Isi Additional Quantity `4`
28. Klik `[Submit]`
29. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idFree4}`
30. Pulihkan jam server dan jam browser ke waktu nyata
31. Ketik Search `{idFree4}`, tekan Enter
32. Klik row action `Allocation Log` pada baris `{idFree4}`
33. Verifikasi entri Allocation Log berjudul `Allocation created by Hendra W`
34. Verifikasi Description entri memuat `Product: FAMS`, `License Type: Concurrent User`, `Target: SUBS-20260101-A1B2C`, `Quantity: +4`, `Cost: Free`
35. Verifikasi header modal `Paid From:` menampilkan `—`
36. Verifikasi tidak ada baris `Resubmitted From` pada entri
37. Tutup modal Allocation Log

## Notes

- Alasan di atas sekitar 35 langkah (37 langkah; dua langkah baseline Allocation ID ikut menambah hitungan): kedua blok satu topik (pencatatan Create oleh Principal Hendra Wijaya pada tiga surface dan Allocation Log), satu kelas harness fungsional, masing-masing memakai record hasil Submit sendiri sehingga berdiri sendiri; blok baca-log berpola tidak dihitung pada ambang smell.
- Langkah penghubung (S-03, R-16): langkah 10, 14, 17, dan 31 (Search entri atau baris berdasarkan Allocation ID), langkah 12 dan 37 (menutup modal), langkah 20 (kembali ke List), langkah 21 dan 30 (mengatur dan memulihkan jam), langkah 1 dan 22 (mencatat baseline Allocation ID halaman pertama tab Current sebelum [Submit]; baris baru adalah baris yang tidak ada di baseline).
- Langkah 36 adalah asersi absence atas satu baris pada modal yang sudah terbuka dan memuat entri `{idFree4}`; langkah 33 sampai 35 pada modal yang sama menjadi anchor positifnya.
- Temuan untuk QA:
  - TC-AC-LA-384 tidak menyebut cara menemukan entri di tiga surface maupun akun System Log aktor; spec memakai Detail User `Hendra Wijaya` dan Search dengan Allocation ID unik.
  - TC-AC-LA-518 butir b menyebut header modal `Paid From:` bernilai `—` tanpa menyatakan bahwa header itu bagian dari modal Allocation Log yang sama dengan entri; spec membaca header pada modal yang sama.
  - TC-AC-LA-518 menyebut tanggal acuan 22 Dec 2026 meski Cost Free tidak bergantung tanggal; spec tetap mengikuti TC.
