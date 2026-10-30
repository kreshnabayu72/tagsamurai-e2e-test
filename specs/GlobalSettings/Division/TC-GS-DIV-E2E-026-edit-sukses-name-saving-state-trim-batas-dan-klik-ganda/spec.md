---
id: TC-GS-DIV-E2E-026-edit-sukses-name-saving-state-trim-batas-dan-klik-ganda
title: "Edit Division Sukses: Saving State, Trim Name, Batas 120 Karakter, Hanya Name, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-82
  - TC-GS-DIV-85
  - TC-GS-DIV-86
  - TC-GS-DIV-101
  - TC-GS-DIV-112
coverage:
  web: automated
---

# Edit Division Sukses: Saving State, Trim Name, Batas 120 Karakter, Hanya Name, dan Klik Ganda

## Prerequisites

- Mode: FE+BE, dengan intercept parsial di atas backend nyata (TC-GS-DIV-82 dan TC-GS-DIV-112).
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var), lalu sesi dipakai sepanjang spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (seeding Division lewat API di hook `before`; target Edit milik spec ini, pengganti `Accounting`, `Administration`, `Audit`, dan `Sales` pada TC sumber; tidak menumpang spec lain atau Population D-02). Code memakai nilai literal karena asersi TC-GS-DIV-101 bergantung pada Code yang tidak berubah:
  - `Saving {runId}-026` dengan Code `E26A` (TC-GS-DIV-82), diubah menjadi `Saving Team {runId}-026`.
  - `Administration {runId}-026` dengan Code `E26B` (TC-GS-DIV-85), diubah menjadi `  General Administration {runId}-026  ` (disimpan `General Administration {runId}-026`).
  - `Audit {runId}-026` dengan Code `E26C` (TC-GS-DIV-86), diubah menjadi nama 120 karakter literal TC `Auditing! of Corporate Strategy and Long Range Planning for Regional Expansion and Partnership Development Programs APAC` (nilai batas TC; tanpa suffix `{runId}`, keunikan antar-run dijamin cleanup di hook `before` dan `after` yang menghapus Division bernama itu).
  - `Accounting {runId}-026` dengan Code `E26D` (TC-GS-DIV-101), diubah menjadi `Accounting and Tax {runId}-026`; Code tetap `E26D`.
  - `Sales {runId}-026` dengan Code `E26E` (TC-GS-DIV-112), diubah menjadi `Sales and Marketing {runId}-026`.
- Cleanup di hook `after` (tidak berasumsi seeding atau rename berhasil penuh): hapus lewat API Division bernama `Saving {runId}-026`, `Saving Team {runId}-026`, `Administration {runId}-026`, `General Administration {runId}-026`, `Audit {runId}-026`, nama 120 karakter literal TC-GS-DIV-86, `Accounting {runId}-026`, `Accounting and Tax {runId}-026`, `Sales {runId}-026`, dan `Sales and Marketing {runId}-026`, serta Division berkode `E26A` sampai `E26E`, bila masih ada. Hook `before` juga menghapus lewat API sisa Division bernama 120 karakter literal itu dari run sebelumnya. Hook `beforeEach`: tutup dialog atau modal yang terbuka lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons request Edit Division selama 3 detik (TC-GS-DIV-82 dan TC-GS-DIV-112) lalu melepasnya; memuat ulang halaman (F5); membuka Modal Changelog untuk menghitung entri; menunggu respons `POST /v2/iam/divisions/check-availability` selesai (dipakai sebelum asersi tidak ada error pada Name).
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-DIV-85: Edit Division Name dengan spasi depan dan belakang disimpan ter-trim

1. Ketik Search `Administration {runId}-026`, tekan Enter
2. Buka row action baris `Administration {runId}-026` lalu klik `Edit`
3. Ganti isi Division Name dengan `  General Administration {runId}-026  ` (spasi di awal dan akhir)
4. Klik `[Save]`
5. Verifikasi toast sukses: `Success, division has been updated.`
6. Ganti isi kotak search dengan `General Administration {runId}-026`, tekan Enter
7. Verifikasi tabel menampilkan Name `General Administration {runId}-026` tanpa spasi di awal dan akhir

### TC-GS-DIV-86: Edit Division Name tepat 120 karakter berhasil disimpan

8. Ganti isi kotak search dengan `Audit {runId}-026`, tekan Enter
9. Buka row action baris `Audit {runId}-026` lalu klik `Edit`
10. Ganti isi Division Name dengan string 120 karakter `Auditing! of Corporate Strategy and Long Range Planning for Regional Expansion and Partnership Development Programs APAC`
11. Tunggu respons check-availability selesai
12. Verifikasi tidak ada error pada Division Name
13. Klik `[Save]`
14. Verifikasi toast sukses: `Success, division has been updated.`
15. Ganti isi kotak search dengan `Auditing! of Corporate Strategy and Long Range Planning for Regional Expansion and Partnership Development Programs APAC`, tekan Enter
16. Verifikasi tabel menampilkan Name baru utuh 120 karakter

### TC-GS-DIV-101: Edit hanya Division Name berhasil dan Code tidak berubah

17. Ganti isi kotak search dengan `Accounting {runId}-026`, tekan Enter
18. Catat nilai Last Updated baris `Accounting {runId}-026`
19. Buka row action baris `Accounting {runId}-026` lalu klik `Edit`
20. Ubah Division Name menjadi `Accounting and Tax {runId}-026`
21. Klik `[Save]`
22. Verifikasi toast sukses: `Success, division has been updated.`
23. Verifikasi modal Edit tertutup
24. Muat ulang halaman (F5)
25. Ketik Search `Accounting and Tax {runId}-026`, tekan Enter
26. Verifikasi baris menampilkan Name `Accounting and Tax {runId}-026`
27. Verifikasi baris menampilkan Code `E26D` (tidak berubah)
28. Verifikasi Last Updated baris diperbarui (lebih baru daripada nilai yang dicatat pada langkah 18)

### TC-GS-DIV-82: Tombol Save masuk Saving state dan seluruh kontrol form disabled

29. Ganti isi kotak search dengan `Saving {runId}-026`, tekan Enter
30. Buka row action baris `Saving {runId}-026` lalu klik `Edit`
31. Pasang intercept yang menahan respons request Edit Division selama 3 detik
32. Ubah Division Name menjadi `Saving Team {runId}-026`
33. Klik `[Save]`
34. Verifikasi tombol `[Save]` menampilkan spinner
35. Verifikasi tombol `[Save]` disabled
36. Verifikasi field Division Name disabled hingga proses simpan selesai
37. Verifikasi field Code disabled hingga proses simpan selesai
38. Verifikasi tombol `[Clear Field]` disabled hingga proses simpan selesai
39. Verifikasi icon `[✕]` disabled hingga proses simpan selesai
40. Lepas intercept respons Edit Division dan tunggu hingga modal Edit tertutup

### TC-GS-DIV-112: Klik ganda Save hanya menyimpan satu kali

41. Ganti isi kotak search dengan `Sales {runId}-026`, tekan Enter
42. Buka row action baris `Sales {runId}-026` lalu klik `Edit`
43. Ubah Division Name menjadi `Sales and Marketing {runId}-026`
44. Pasang intercept yang menahan respons request Edit Division selama 3 detik
45. Klik `[Save]` dua kali cepat
46. Verifikasi tombol `[Save]` disabled setelah klik pertama
47. Lepas intercept respons Edit Division
48. Verifikasi tepat satu toast sukses: `Success, division has been updated.`
49. Buka Modal Changelog
50. Verifikasi Changelog mencatat tepat satu entri Edit Name dari `Sales {runId}-026` menjadi `Sales and Marketing {runId}-026`
51. Tutup Modal Changelog

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-82, 85, 86, 101, 112). Mode: FE+BE (intercept parsial untuk penahan respons). Kelas harness: aksi sukses.
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC berbeda dari urutan nomor TC sumber: kasus tanpa intercept lebih dulu (TC-85, TC-86, TC-101), lalu dua kasus dengan penahan respons berurutan (TC-82, TC-112) supaya intercept dipasang dan dilepas dalam satu blok. Setiap TC memakai Division milik spec sendiri sehingga urutan tidak saling bergantung.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, 17, 25, 29, 41 (mencari target Edit atau baris hasil lewat Search; Search diganti nilai baru pada pencarian berikutnya); langkah 6 dan 15 (mencari nama hasil rename untuk diverifikasi); langkah 11 (menunggu respons check-availability selesai sebelum asersi tidak ada error pada langkah 12); langkah 18 (mencatat Last Updated sebagai pembanding); langkah 40, 44, dan 47 (melepas dan memasang intercept; langkah 31 adalah langkah 2 TC-GS-DIV-82 dan langkah 24 adalah bagian langkah 4 TC-GS-DIV-101); langkah 49 dan 51 (membuka dan menutup Modal Changelog).
- Langkah 44 dan 47 (memasang dan melepas penahan respons pada TC-GS-DIV-112) tidak ada di Langkah Uji TC sumber. Penahan respons ditambahkan supaya Expected a ("Tombol `[Save]` disabled setelah klik pertama") dapat diamati sebelum respons selesai; tanpa penahan, state itu berlalu sebelum asersi.
- Langkah 50: nama lama dan baru mengandung `{runId}-026`, sehingga pasangan Old Value dan New Value itu unik per run dan hitungan "tepat satu entri" tidak memerlukan baseline.
- Asersi "hanya 1 perubahan tersimpan" pada TC-GS-DIV-112 diwujudkan lewat langkah 48 (tepat satu toast sukses) dan langkah 50 (tepat satu entri Changelog).
- Spec melewati sekitar 35 langkah (51 langkah) karena memuat lima TC aksi sukses yang masing-masing mengedit Division sendiri; seluruhnya satu kelas harness (aksi sukses), tiap blok memakai data dan form sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-GS-DIV-101 butir d ("Last Updated baris diperbarui") dapat tidak teramati bila format Last Updated tidak menampilkan detik dan Edit terjadi di menit yang sama dengan seeding; TC tidak memberi nilai pembanding. Spec membandingkan dengan nilai yang dicatat sebelum Save.
  - TC-GS-DIV-82 tidak menyebut hasil akhir Save setelah respons dilepas; spec hanya menunggu modal tertutup tanpa asersi toast.
  - TC-GS-DIV-112 tidak menyebut cara mengamati state sesudah klik pertama; lihat Notes mengenai penahan respons.
