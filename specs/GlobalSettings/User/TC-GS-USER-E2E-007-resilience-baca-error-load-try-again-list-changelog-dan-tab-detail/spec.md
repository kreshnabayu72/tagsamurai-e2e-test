---
id: TC-GS-USER-E2E-007-resilience-baca-error-load-try-again-list-changelog-dan-tab-detail
title: "Resilience Baca User: Error Load User List, Modal Changelog, dan Tab System Log User Detail dengan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-23
  - TC-GS-USER-994
  - TC-GS-USER-995
  - TC-GS-USER-1069
  - TC-GS-USER-1070
coverage:
  web: automated
---

# Resilience Baca User: Error Load User List, Modal Changelog, dan Tab System Log User Detail dengan Try Again

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness fault injection).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): John Doe (No. 18) dan Dewi Lestari (No. 12). Spec tidak membuat, mengubah, atau menghapus data backend.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script (tidak disebut di TC dan PRD):
  - Respons daftar User: jawab 5xx (500) (langkah 1 sampai 6, TC-GS-USER-23).
  - Respons Changelog User: jawab 5xx (500) (langkah 9 sampai 14, TC-GS-USER-994); tahan 3 detik lalu jawab 5xx (500) (langkah 16 sampai 22, TC-GS-USER-1069). Tiap intercept dilepas sebelum langkah `[Try Again]` atau sebelum TC berikutnya.
  - Respons System Log User Detail: jawab 5xx (500) (langkah 27 sampai 32, TC-GS-USER-995); tahan 3 detik lalu jawab 5xx (500) (langkah 36 sampai 41, TC-GS-USER-1070).
- Pemulihan di hook `after`: semua intercept dilepas walau spec gagal di tengah.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-USER-23: Error load User List menampilkan state error dengan tombol retry

1. Pasang intercept pada respons daftar User: jawab 5xx
2. Buka Global Settings > User
3. Verifikasi tabel menampilkan teks `"Unable to load this data."`
4. Verifikasi tombol `[Try Again]` tampil
5. Verifikasi tabel tidak menampilkan empty state
6. Lepas intercept respons daftar User sehingga endpoint pulih
7. Klik `[Try Again]`
8. Verifikasi data tabel User List dimuat ulang dan tampil

### TC-GS-USER-994: Error load Modal Changelog User menampilkan state error dengan [Try Again]

9. Pasang intercept pada respons Changelog User: jawab 5xx
10. Klik icon Changelog
11. Verifikasi Modal Changelog menampilkan teks `"Unable to load this data."`
12. Verifikasi Modal Changelog menampilkan tombol `[Try Again]`
13. Verifikasi Modal Changelog tidak menampilkan empty state
14. Lepas intercept respons Changelog User
15. Tutup Modal Changelog dengan klik `✕`

### TC-GS-USER-1069: Modal Changelog User menampilkan Loading lalu Error load saat fetch gagal

16. Pasang intercept pada respons Changelog User: tahan 3 detik lalu jawab 5xx
17. Klik icon Changelog di Table Tools
18. Verifikasi tabel Modal Changelog menampilkan skeleton rows selama memuat
19. Verifikasi setelah fetch gagal Modal Changelog menampilkan teks `"Unable to load this data."`
20. Verifikasi setelah fetch gagal Modal Changelog menampilkan tombol `[Try Again]`
21. Verifikasi Modal Changelog tidak menampilkan empty state
22. Lepas intercept respons Changelog User sehingga endpoint pulih
23. Klik `[Try Again]`
24. Verifikasi data changelog tampil
25. Tutup Modal Changelog dengan klik `✕`

### TC-GS-USER-995: Error load tab di User Detail menampilkan state error dengan [Try Again]

26. Klik icon Search, ketik `John Doe`, tekan Enter
27. Pasang intercept pada respons System Log User Detail: jawab 5xx
28. Klik Name `John Doe` di User List
29. Klik Tab `System Log`
30. Verifikasi Tab System Log menampilkan teks `"Unable to load this data."`
31. Verifikasi Tab System Log menampilkan tombol `[Try Again]`
32. Lepas intercept respons System Log User Detail

### TC-GS-USER-1070: Tab System Log menampilkan Loading lalu Error load saat fetch gagal

33. Klik menu User di sidebar Global Settings
34. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
35. Klik Name `Dewi Lestari` di User List
36. Pasang intercept pada respons System Log User Detail: tahan 3 detik lalu jawab 5xx
37. Klik Tab `System Log`
38. Verifikasi tabel Tab System Log menampilkan skeleton rows selama memuat
39. Verifikasi setelah fetch gagal Tab System Log menampilkan teks `"Unable to load this data."`
40. Verifikasi setelah fetch gagal Tab System Log menampilkan tombol `[Try Again]`
41. Lepas intercept respons System Log User Detail sehingga endpoint pulih
42. Klik `[Try Again]`
43. Verifikasi data System Log tampil

## Notes

- Mode: FE+BE (intercept parsial, kelas harness b: fault injection; bagian 6 konvensi). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (43 langkah) karena kelima TC berkelas harness yang sama (b, kegagalan 5xx pada pembacaan data) dan permukaan baca yang sama (User List, Modal Changelog, Tab System Log); tiap blok TC berdiri sendiri (intercept sendiri, dilepas di akhir blok) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-USER-1069 ditaruh sebelum TC-GS-USER-995 supaya dua TC Modal Changelog berurutan di User List, lalu TC-GS-USER-995 dan TC-GS-USER-1070 berurutan di User Detail (menghindari bolak-balik antara User List dan User Detail).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 6, 9, 14, 16, 22, 27, 32, 36, dan 41 (pasang dan lepas intercept), 15 dan 25 (tutup Modal Changelog), 26, 33, dan 34 (mencari dan membuka baris target, karena baris John Doe dan Dewi Lestari tidak selalu berada di halaman 1), 35 (membuka User Detail Dewi Lestari, precondition TC-GS-USER-1070).
- Langkah 3, 11, 19, dan 30 menyatakan tanda kutip ganda yang tertulis di Expected TC (`"Unable to load this data."`).
- Temuan untuk QA:
  - TC-GS-USER-23 precondition menyebut "Manual Only, dipicu via mock/proxy" sedangkan kolom Automation bernilai Automatable; spec memicu lewat `Spectra.intercept()` di atas backend nyata.
  - TC-GS-USER-23, 994, 995, 1069, dan 1070 tidak menyebut nama endpoint yang digagalkan; ditentukan tim FE.
  - TC-GS-USER-1069 dan 1070 menyebut "dibuat lambat lalu gagal" tanpa durasi; spec memakai tahan 3 detik.
  - TC-GS-USER-1069 dan 1070 Expected c ("data changelog/System Log tampil") mengandaikan data riwayat sudah ada pada Dewi Lestari dan entitas uji; Tabel Pre-setup tidak menyebut isi log. Spec mengasersi tampilnya sedikitnya satu baris data.
  - TC-GS-USER-995 tidak memuat langkah `[Try Again]` pada Expected; spec hanya mengasersi state error sesuai TC (klik `[Try Again]` diuji di TC-GS-USER-1070).
  - TC-GS-USER-994 dan 1069 beririsan (Modal Changelog gagal 5xx); spec memuat keduanya karena TC-GS-USER-994 tidak mensyaratkan jeda Loading dan TC-GS-USER-1069 mensyaratkan jeda dan `[Try Again]`.
