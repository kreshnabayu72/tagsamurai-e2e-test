---
id: TC-GS-USER-E2E-069-resilience-download-gagal-toast-error-semua-permukaan
title: "Resilience Download User: Toast Error dengan Nama Berkas pada User List, Modal Changelog User, Modal Changelog User > Role, serta Tab Changelog, System Log, User Log, dan Non-Login User Detail"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-460
  - TC-GS-USER-1055
  - TC-GS-USER-1056
  - TC-GS-USER-1057
  - TC-GS-USER-1058
  - TC-GS-USER-1059
  - TC-GS-USER-1060
coverage:
  web: automated
---

# Resilience Download User: Toast Error dengan Nama Berkas pada User List, Modal Changelog User, Modal Changelog User > Role, serta Tab Changelog, System Log, User Log, dan Non-Login User Detail

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness b: fault injection, bagian 3 prinsip 13 dan bagian 6 konvensi).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): Dewi Lestari (No. 12), dibuka di Detail untuk tab Role, Changelog, System Log, User Log, dan Non-Login User. Spec tidak membuat, mengubah, atau menghapus data backend; download yang digagalkan tidak mengubah data. Nama berkas pada toast mengikuti nama user `Dewi Lestari` tanpa suffix (`Dewi-Lestari`).
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint ditentukan tim FE di tahap script (tidak disebut di TC dan PRD). Jawaban 5xx (500) diberikan tanpa meneruskan request ke backend, satu intercept per permukaan, dan dilepas segera setelah toast hasilnya tampil:
  - Respons download User List (TC-GS-USER-460).
  - Respons download Modal Changelog User (TC-GS-USER-1055).
  - Respons download Modal Changelog User > Role (TC-GS-USER-1056).
  - Respons download Tab Changelog Detail (TC-GS-USER-1057).
  - Respons download Tab System Log Detail (TC-GS-USER-1058).
  - Respons download Tab User Log Detail (TC-GS-USER-1059).
  - Respons download Tab Non-Login User Detail (TC-GS-USER-1060).
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD): mengamati bahwa tidak ada berkas terunduh (event download browser) pada permukaan yang Expected-nya menyebut "Tidak ada file terunduh".
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah): lepas semua intercept, tutup Modal Changelog yang masih terbuka, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-USER-460: User List, Download gagal memunculkan toast error

1. Pasang intercept pada respons download User List: jawab 5xx
2. Klik icon Download di Table Tools
3. Klik `Download as CSV`
4. Verifikasi toast error: "Error, failed to download User."
5. Lepas intercept respons download User List
6. Verifikasi tidak ada berkas terunduh

### TC-GS-USER-1055: Modal Changelog User, Download gagal memunculkan toast error dengan nama berkas permukaan

7. Klik icon Changelog di Table Tools
8. Pasang intercept pada respons download Modal Changelog User: jawab 5xx
9. Klik icon Download pada Modal Changelog User
10. Klik `Download as CSV`
11. Verifikasi toast error: "Error, failed to download Changelog-User."
12. Lepas intercept respons download Modal Changelog User
13. Verifikasi tidak ada berkas terunduh
14. Tutup Modal Changelog User dengan klik `✕`

### TC-GS-USER-1056: Modal Changelog User > Role, Download gagal memunculkan toast error dengan nama berkas permukaan

15. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
16. Klik Name `Dewi Lestari` di User List
17. Klik Tab `Role`
18. Klik icon Changelog di toolbar Tab Role
19. Pasang intercept pada respons download Modal Changelog User > Role: jawab 5xx
20. Klik icon Download pada Modal Changelog
21. Klik `Download as CSV`
22. Verifikasi toast error: "Error, failed to download Changelog-Dewi-Lestari-Global-Role."
23. Lepas intercept respons download Modal Changelog User > Role
24. Verifikasi tidak ada berkas terunduh
25. Tutup Modal Changelog dengan klik `✕`

### TC-GS-USER-1057: Tab Changelog Detail, Download gagal memunculkan toast error dengan nama berkas permukaan

26. Klik Tab `Changelog`
27. Pasang intercept pada respons download Tab Changelog: jawab 5xx
28. Klik icon Download pada Tab Changelog
29. Klik `Download as CSV`
30. Verifikasi toast error: "Error, failed to download Changelog-Dewi-Lestari."
31. Lepas intercept respons download Tab Changelog
32. Verifikasi tidak ada berkas terunduh

### TC-GS-USER-1058: Tab System Log Detail, Download gagal memunculkan toast error dengan nama berkas permukaan

33. Klik Tab `System Log`
34. Pasang intercept pada respons download Tab System Log: jawab 5xx
35. Klik icon Download pada Tab System Log
36. Klik `Download as CSV`
37. Verifikasi toast error: "Error, failed to download System-Log-Dewi-Lestari."
38. Lepas intercept respons download Tab System Log
39. Verifikasi tidak ada berkas terunduh

### TC-GS-USER-1059: Tab User Log Detail, Download gagal memunculkan toast error dengan nama berkas permukaan

40. Klik Tab `User Log`
41. Pasang intercept pada respons download Tab User Log: jawab 5xx
42. Klik icon Download pada Tab User Log
43. Klik `Download as CSV`
44. Verifikasi toast error: "Error, failed to download User-Log-Dewi-Lestari."
45. Lepas intercept respons download Tab User Log
46. Verifikasi tidak ada berkas terunduh

### TC-GS-USER-1060: Tab Non-Login User Detail, Download gagal memunculkan toast error dengan nama berkas permukaan

47. Klik Tab `Non-Login User`
48. Pasang intercept pada respons download Tab Non-Login User: jawab 5xx
49. Klik icon Download pada Tab Non-Login User
50. Klik `Download as CSV`
51. Verifikasi toast error: "Error, failed to download Non-Login-User-Dewi-Lestari."
52. Lepas intercept respons download Tab Non-Login User
53. Verifikasi tidak ada berkas terunduh

## Notes

- Mode: FE+BE (intercept parsial, kelas harness b: fault injection; bagian 6 konvensi). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (53 langkah). Alasan: ketujuh TC berada di satu kelas harness (b, kegagalan download 5xx), satu akun, dan satu pola langkah di tujuh permukaan tabel; tiap blok TC berdiri sendiri (intercept sendiri, dilepas di dalam blok) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber dipertahankan (460, 1055, 1056, 1057, 1058, 1059, 1060): User List, Modal Changelog User, lalu Detail Dewi Lestari dengan tab Role, Changelog, System Log, User Log, dan Non-Login User berurutan dalam satu pembukaan Detail.
- Langkah penghubung (aksi tanpa `Verifikasi`): memasang dan melepas intercept, Search `Dewi Lestari` dan membuka Detail (baris Dewi Lestari tidak selalu berada di halaman 1), berpindah tab, membuka Modal Changelog, dan menutup Modal Changelog dengan `✕`.
- Pembagian TC lintas spec: isi berkas Download User List diverifikasi di spec 076 dan Download yang berhasil pada permukaan lain di spec permukaan masing-masing; spec ini hanya memuat jalur kegagalan download.
- Temuan untuk QA:
  - TC-GS-USER-460, 1055, 1056, 1057, 1058, 1059, dan 1060 menulis "Endpoint download dibuat gagal 5xx" tanpa nama endpoint; spec memicu lewat `Spectra.intercept()` di atas backend nyata dan nama endpoint ditentukan tim FE di tahap script.
  - TC-GS-USER-460 dan 1055 sampai 1060 menyebut "Tidak ada file terunduh" tanpa cara mengamatinya; spec memakai pengamatan event download browser (kemampuan disediakan tim FE/BE).
  - TC-GS-USER-1056 sampai 1060 menyebut nama berkas dengan nama user `Dewi Lestari` (`Dewi-Lestari`); spec memakai Dewi Lestari Pre-setup (No. 12) tanpa suffix supaya nama berkas pada toast sesuai Expected TC. Tidak ada aksi tulis atau hapus pada data itu.
  - TC-GS-USER-1056 menyebut "Klik Download" tanpa menyebut icon; spec memakai icon Download di toolbar Modal Changelog.
