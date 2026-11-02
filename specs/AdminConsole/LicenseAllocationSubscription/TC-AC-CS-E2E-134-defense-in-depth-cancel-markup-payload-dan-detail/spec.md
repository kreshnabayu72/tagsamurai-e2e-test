---
id: TC-AC-CS-E2E-134-defense-in-depth-cancel-markup-payload-dan-detail
title: "Defense-in-Depth: Cancel, Markup, Payload, dan Detail"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-506
  - TC-AC-CS-573
  - TC-AC-CS-611
  - TC-AC-CS-514
  - TC-AC-CS-619
coverage:
  web: automated
---

# Defense-in-Depth: Cancel, Markup, Payload, dan Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request dengan token sesi aktor (login API password, token tidak dihitung sebagai sesi web); membaca jumlah term, trial, transaksi Wallet, dan entri log sebagai state data; `Spectra.intercept()` parsial di atas backend nyata untuk memaksa respons 403 dan 404 pada endpoint Detail term (intercept dilepas segera setelah dipakai, S-09). Path dan body request tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim FE/BE tanpa endpoint karangan (S-13, bagian 8b butir 1); jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; request yang diuji ditolak sehingga tidak ada perubahan data); jumlah term, trial, transaksi Wallet, dan entri log dicatat sebagai baseline sebelum langkah pertama:
  1. TC-AC-CS-506: term `A506` berstatus Archive (setara Pre-setup #58).
  2. TC-AC-CS-573: Client `C573+{runId}-134` binaan Principal tanpa term maupun trial (setara Pre-setup #48).
  3. TC-AC-CS-611: Client `C611+{runId}-134` binaan langsung PT Maju Bersama pada group `Jawa`, dengan trial FAMS Active dan term paid FAMS Waiting for Approval, serta trial SAMS Active dan term paid SAMS Pending (setara Pre-setup #136 dan #137).
  4. TC-AC-CS-514: Client `<b>Evil</b><script>alert(1)</script>+{runId}-134` (binaan langsung PT Maju Bersama) dengan term FAMS Growth Active (setara Pre-setup #107) dan entri Changelog dari pembuatan term.
  5. TC-AC-CS-619: baris `SUBS-20260101-00001` (Pre-setup #61, Active, PT Sejahtera, FAMS, Professional, Plan Owner PT Maju Bersama) dipakai baca-saja; respons Detail dipaksa lewat intercept sehingga data tidak berubah.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-506: Cancel Subscription langsung pada term bukan Active ditolak

1. Kirim POST Cancel Subscription pada term `A506` berstatus Archive dengan token sesi aktor
2. Verifikasi respons server menolak dan data term tidak berubah
3. Verifikasi tidak ada efek tambahan pada Wallet (jumlah transaksi sama dengan baseline) maupun log (jumlah entri sama dengan baseline)

### TC-AC-CS-573: Request langsung dengan nilai non-digit pada Duration dan kuota Trial ditolak server

4. Kirim POST Activate Trial Client `C573` Product `FAMS` Plan `Growth` dengan Trial Duration `abc`
5. Verifikasi respons server menolak request
6. Kirim POST Activate Trial yang sama dengan Trial Asset Quota `1.5`
7. Verifikasi respons server menolak request
8. Kirim POST Add Subscription mode New Client `C573` Product `SAMS` Plan `Growth` dengan Duration `1.5`
9. Verifikasi respons server menolak request
10. Verifikasi tidak ada trial maupun term dibuat untuk Client `C573` (jumlah sama dengan baseline)

### TC-AC-CS-611: Convert mode New langsung saat Client dan Product hanya punya term paid Waiting for Approval atau Pending ditolak

11. Kirim POST Convert mode New dari trial FAMS Client `C611` Plan `Growth` Duration `1` Start Date `19/08/26`
12. Verifikasi respons server menolak dengan pesan "This client already has an active subscription for this product."
13. Kirim POST Convert mode New dari trial SAMS Client `C611` Plan `Growth` Duration `1` Start Date `19/08/26`
14. Verifikasi respons server menolak dengan pesan "This client already has an active subscription for this product."
15. Verifikasi trial FAMS dan trial SAMS tetap Active dan tidak menjadi Converted
16. Verifikasi term paid Waiting for Approval dan term paid Pending tidak berubah dan tidak ada term baru

### TC-AC-CS-514: Nilai berisi markup pada nama Client dirender sebagai teks

17. Ketik Search `Evil</b><script>alert(1)</script>+{runId}-134`, tekan Enter
18. Verifikasi nama Client `<b>Evil</b><script>alert(1)</script>+{runId}-134` tampil apa adanya sebagai teks pada tabel tab `Current`
19. Klik ikon Changelog
20. Ketik Search `Evil</b><script>alert(1)</script>+{runId}-134`, tekan Enter pada modal Changelog
21. Verifikasi nama Client tampil apa adanya sebagai teks pada Changelog
22. Klik `[✕]`
23. Klik baris term Client itu
24. Verifikasi nama Client tampil apa adanya sebagai teks pada Subscription Detail
25. Verifikasi tidak ada tag HTML yang dirender dan tidak ada skrip berjalan (tidak ada dialog `alert`) pada tabel, Changelog, dan Detail

### TC-AC-CS-619: Detail ditolak server karena di luar scope atau record sudah tidak ada

26. Klik menu `Client Subscription` di sidebar
27. Ketik Search `SUBS-20260101-00001`, tekan Enter
28. Paksa respons endpoint Detail 403 lewat `Spectra.intercept()`
29. Klik baris `SUBS-20260101-00001`
30. Verifikasi toast error "You don't have permission to do this."
31. Verifikasi UI di-refresh sehingga elemen yang tidak berhak tersembunyi
32. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
33. Verifikasi Detail tidak terbuka
34. Lepas intercept respons 403
35. Klik menu `Client Subscription` di sidebar
36. Ketik Search `SUBS-20260101-00001`, tekan Enter
37. Paksa respons endpoint Detail 404 lewat `Spectra.intercept()`
38. Klik baris `SUBS-20260101-00001`
39. Verifikasi toast netral "This subscription is no longer available."
40. Verifikasi List dimuat ulang
41. Verifikasi Detail tidak terbuka
42. Lepas intercept respons 404

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a (defense-in-depth) dengan Expected berupa respons API tetap masuk spec FE+BE walau tumpang tindih dengan `tc-license-allocation-subscription-backend.md`; asersi hanya respons server dan state data (bagian 8b butir 1). TC-AC-CS-514 dan TC-AC-CS-619 mengasersi tampilan FE atas input markup dan atas respons 403/404 yang dipaksa.
- Spec ini melewati ~35 langkah (42). Alasan: semua blok satu kelas harness (defense-in-depth server terhadap input dan akses tidak sah) dan berdiri sendiri dengan data milik spec; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan tidak ada langkah prefix yang dapat dihapus.
- Langkah penghubung (S-03): langkah 22 (menutup modal), langkah 17 dan 20 (Search memakai potongan nama bermarkup yang berurutan dan memuat suffix, `Evil</b><script>alert(1)</script>+{runId}-134`, supaya cocok sebagai substring nama Client; R-16), langkah 26 dan 35 (muat ulang List), langkah 27 dan 36 (Search untuk menemukan baris target, R-16), langkah 34 dan 42 (melepas intercept segera setelah dipakai, S-09).
- Langkah 30 sampai 33 dan 39 sampai 41 memakai intercept pada endpoint Detail yang dinamai TC; baris `SUBS-20260101-00001` tidak berubah.
- Temuan untuk QA:
  - TC-AC-CS-506, 573 Expected a menyebut "ditolak" tanpa pesan atau kode status; spec mengasersi penolakan tanpa teks (S-02). TC-AC-CS-506 Expected b ("tidak ada efek tambahan pada Wallet maupun log") tidak menyebut surface log yang diperiksa; spec memakai jumlah entri log seluruh surface yang dibaca fixture BE.
  - TC-AC-CS-514 Expected b ("tidak ada skrip berjalan") tidak menyebut cara mengamati; spec memakai tidak adanya dialog `alert` dan menyatakan kemampuan pengamatan dialog pada tim FE.
  - TC-AC-CS-619 adalah TC pemaksaan respons (403/404 pada endpoint Detail) yang masuk kelas fault injection ringan; ditempatkan di spec defense-in-depth sesuai pemetaan perencana. Paksa 403 tidak benar-benar mewakili aktor di luar scope.
  - TC-AC-CS-611 Expected c ("tidak ada term baru") tidak menyebut kolom pembanding; spec membandingkan jumlah term dengan baseline.
