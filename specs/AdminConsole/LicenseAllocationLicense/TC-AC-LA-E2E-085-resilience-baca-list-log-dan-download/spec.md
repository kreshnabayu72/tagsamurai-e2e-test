---
id: TC-AC-LA-E2E-085-resilience-baca-list-log-dan-download
title: "Resilience Baca: Error Load List, Allocation Log, Modal Changelog, dan Download Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-14
  - TC-AC-LA-15
  - TC-AC-LA-46
  - TC-AC-LA-347
  - TC-AC-LA-358
  - TC-AC-LA-381
coverage:
  web: automated
---

# Resilience Baca: Error Load List, Allocation Log, Modal Changelog, dan Download Gagal

## Prerequisites

- Mode: FE+BE. Spec memakai `Spectra.intercept()` parsial di atas backend nyata; intercept dilepas segera setelah pemicu selesai (S-09). TC tidak menyebut endpoint, dan openapi.yaml serta LLD modul tidak ada, sehingga pola endpoint yang di-intercept disediakan tim FE (S-13): GET list License Allocation, GET log Allocation Log, GET data Modal Changelog, serta permintaan Download tab Current, Download tab History, dan Download Changelog.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): Data Seed minimal 30 alokasi lintas enam status (#54) dengan 25 entri Changelog, dan alokasi dengan riwayat log lengkap (#55) sebagai baris tempat Allocation Log dibuka.
- Kemampuan teknis (disediakan tim FE): menahan respons list/Changelog (respons ditahan) untuk mengamati Loading, membalas intercept dengan 500 sekali lalu 200 pada permintaan berikutnya, dan melepas semua intercept.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-14: Error load List menampilkan state error dengan Try Again

1. Pasang intercept GET list License Allocation: respons 500
2. Buka Allocation > License Allocation
3. Verifikasi area tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
4. Verifikasi empty state tidak tampil
5. Lepas intercept GET list

### TC-AC-LA-15: Try Again memuat ulang List setelah error load

6. Pasang intercept GET list License Allocation: respons pertama 500, respons berikutnya 200
7. Buka Allocation > License Allocation hingga state error tampil
8. Klik `[Try Again]`
9. Verifikasi request list dikirim ulang
10. Verifikasi tabel tampil dengan baris data
11. Verifikasi state error hilang
12. Lepas intercept GET list

### TC-AC-LA-46: Error muat Allocation Log menampilkan Try Again

13. Pasang intercept GET log Allocation Log: respons pertama 500, respons berikutnya 200
14. Klik row action `Allocation Log` pada alokasi dengan riwayat log lengkap (#55)
15. Verifikasi modal menampilkan `Unable to load this data.` dengan `[Try Again]`
16. Klik `[Try Again]`
17. Verifikasi daftar log tampil
18. Lepas intercept GET log dan tutup modal Allocation Log

### TC-AC-LA-347: Download gagal menampilkan toast error dengan nama berkas tab

19. Pasang intercept permintaan Download: respons 500
20. Klik `Download as CSV` pada tab Current
21. Verifikasi toast error "Error, failed to download License-Allocation-Current."
22. Tutup toast error tab Current
23. Klik tab `History`
24. Klik `Download as CSV`
25. Verifikasi toast error "Error, failed to download License-Allocation-History."
26. Lepas intercept permintaan Download

### TC-AC-LA-358: Empty filtered, loading, dan error load pada Modal Changelog

27. Klik tab `Current`
28. Klik ikon `Changelog` untuk membuka Modal Changelog
29. Ketik Search `zzzzqqqq` di Search Changelog, tekan Enter
30. Verifikasi Title `No results found` dan Description `Try adjusting your search or filter.`
31. Tutup Modal Changelog
32. Pasang intercept GET Changelog: respons ditahan
33. Buka Modal Changelog
34. Verifikasi komponen DataTable Loading tampil
35. Lepas intercept GET Changelog dan tutup Modal Changelog
36. Pasang intercept GET Changelog: respons pertama 500, respons berikutnya 200
37. Buka Modal Changelog
38. Verifikasi `Unable to load this data.` dengan `[Try Again]` tampil
39. Klik `[Try Again]`
40. Verifikasi `[Try Again]` memuat ulang data Changelog
41. Lepas intercept GET Changelog dan tutup Modal Changelog

### TC-AC-LA-381: Download Changelog gagal menampilkan toast error

42. Pasang intercept permintaan Download Changelog: respons 500
43. Buka Modal Changelog dan klik `Download as CSV`
44. Verifikasi toast error "Error, failed to download Changelog-License-Allocation."
45. Lepas intercept permintaan Download Changelog dan tutup Modal Changelog

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 6, 12, 13, 18, 19, 26, 32, 35, 36, 41, 42, 45 (memasang dan melepas intercept, S-09), 22 (dismiss toast sebelum asersi toast berikutnya, R-12), 23, 27, dan 28 (membuka tab dan Modal Changelog; langkah 27 mengembalikan ke tab `Current` karena ikon `Changelog` hanya ada di tab Current, S-14), 31 (menutup modal), 29 (Search Changelog, R-16).
- Spec melewati sekitar 35 langkah. Alasan pertahanan: seluruh blok satu kelas harness (fault injection pada baca) dengan pola pasang-intercept, amati, lepas, dan tiap blok berdiri sendiri; langkah pasang dan lepas intercept adalah langkah penghubung.
- Temuan untuk QA:
  - TC-AC-LA-14 sampai 381 tidak menyebut endpoint yang di-intercept; disediakan tim FE (S-13).
  - TC-AC-LA-15 Precondition c dan TC-AC-LA-46 menyebut urutan respons "500 lalu 200" tanpa menyebut cara; spec memakai intercept urutan-respons yang disediakan tim FE.
  - TC-AC-LA-358 Langkah 2 ("Muat ulang dengan respons ditahan lalu dengan respons 500") tidak menyebut apakah memuat ulang halaman atau membuka ulang Modal; spec membuka ulang Modal Changelog.
  - TC-AC-LA-358 Expected b ("komponen DataTable Loading") tidak menyebut teks atau elemen; diasersi sebagai komponen Loading tampil.
  - TC-AC-LA-347 dan TC-AC-LA-381 Expected tidak menyebut apakah file terunduh; tidak diasersi.
