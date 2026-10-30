---
id: TC-GS-DIV-E2E-011-create-validasi-name-batas-karakter-emoji-dan-duplikat
title: "Create Division: Validasi Name (Kosong, Spasi, 121 Karakter, Emoji, Duplikat)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-34
  - TC-GS-DIV-35
  - TC-GS-DIV-38
  - TC-GS-DIV-39
  - TC-GS-DIV-40
  - TC-GS-DIV-41
  - TC-GS-DIV-42
coverage:
  web: automated
---

# Create Division: Validasi Name (Kosong, Spasi, 121 Karakter, Emoji, Duplikat)

## Prerequisites

- Mode: FE+BE (backend nyata; TC-GS-DIV-40, TC-GS-DIV-41, dan TC-GS-DIV-42 butuh pengecekan keunikan Division Name ke backend).
- Akun aktor: Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec): Division `Finance` (Code `FIN`) sebagai nama yang sudah ada untuk TC-GS-DIV-40, TC-GS-DIV-41, dan TC-GS-DIV-42.
- Data uji: semua nilai hanya diketik dan seluruh submit diblokir, sehingga tidak ada Division yang dibuat dan tidak ada seeding. Nilai TC-GS-DIV-35 adalah 3 spasi; nilai TC-GS-DIV-40 adalah `FINANCE`; nilai TC-GS-DIV-41 adalah `  finance  ` (2 spasi di depan dan belakang); nilai TC-GS-DIV-42 adalah `Finance`. Nilai TC-GS-DIV-38 adalah 121 karakter `Divisions of Corporate Strategy and Long Range Planning for Regional Expansion and Partnership Development Programs APACs`; nilai TC-GS-DIV-39 adalah `Finance 😀`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `before`: mencatat jumlah Division sebagai baseline (dipakai langkah 5, 10, dan 40).
- Hook `afterEach`: tutup modal Create yang masih terbuka dan dirty lewat `✕`, lalu klik `[Leave]` pada dialog `Unsaved Changes`, kembali ke layar Division (cadangan bila langkah 44 sampai 46 tidak tercapai).
- Cleanup (hook `after`): bila ada Division tidak terduga yang terbentuk dengan nama dari spec ini (`Finance 😀` atau 121 karakter hasil uji), hapus lewat API; tidak berasumsi langkah UI berhasil.
- Kemampuan teknis: pengetikan karakter demi karakter dan paste via clipboard; penantian debounce ±500 ms; klik `[Submit]` sebelum 500 ms berlalu sejak ketikan terakhir (TC-GS-DIV-42); pembacaan nilai field, panjang nilai, fokus keyboard, dan border field (`severity="danger"`); pembacaan jumlah Division lewat API (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); menahan lalu melepas respons check-availability dengan intercept (endpoint check-availability tercantum di LLD Division), dipakai TC-GS-DIV-40.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- State global: tidak ada yang diubah. Sesi sudah berada di akun default suite (Total Control, Sari Dewi).

## Test Steps

### TC-GS-DIV-34: Submit Create dengan Division Name kosong

1. Klik `[+ Division]`
2. Klik `[Submit]` dengan field Division Name kosong
3. Verifikasi border field Division Name berubah `severity="danger"`
4. Verifikasi pesan error inline di bawah field: `Division Name must not be empty`
5. Verifikasi record tidak dibuat: jumlah Division lewat API sama dengan baseline
6. Verifikasi modal tetap terbuka

### TC-GS-DIV-35: Submit Create dengan Division Name hanya berisi spasi

7. Ketik 3 spasi pada field Division Name
8. Klik `[Submit]`
9. Verifikasi Name diperlakukan kosong: pesan inline `Division Name must not be empty`
10. Verifikasi record tidak dibuat: jumlah Division lewat API sama dengan baseline
11. Verifikasi modal tetap terbuka

### TC-GS-DIV-38: Division Name 121 karakter diterima input dan menampilkan error inline

12. Klik `[Clear Field]`
13. Ketik atau tempel 121 karakter pada field Division Name
14. Verifikasi input menerima seluruh 121 karakter (panjang nilai field 121 karakter, tidak dipotong)
15. Verifikasi error inline `Max. 120 characters` muncul langsung saat melebihi 120 karakter
16. Verifikasi border field Division Name `severity="danger"`
17. Klik `[Submit]`
18. Verifikasi submit diblokir: modal tetap terbuka

### TC-GS-DIV-39: Division Name berisi emoji menampilkan error inline

19. Klik `[Clear Field]`
20. Ketik `Finance 😀` pada field Division Name
21. Verifikasi error inline `Division Name contains invalid characters` muncul langsung saat mengetik
22. Verifikasi border field Division Name `severity="danger"`
23. Klik `[Submit]`
24. Verifikasi submit diblokir: modal tetap terbuka

### TC-GS-DIV-40: Division Name duplikat tanpa membedakan huruf besar kecil menampilkan error setelah debounce

25. Klik `[Clear Field]`
26. Tahan (delay) respons check-availability di network
27. Ketik `FINANCE` pada field Division Name tanpa jeda
28. Verifikasi tidak ada error `Division Name already exists` selama masih mengetik (respons check-availability masih ditahan)
29. Berhenti mengetik ±500 ms dengan kursor tetap berada di field Division Name
30. Lepas tahanan respons
31. Verifikasi error inline `Division Name already exists` muncul setelah debounce
32. Verifikasi error muncul tanpa kursor keluar dari field Division Name

### TC-GS-DIV-41: Division Name duplikat dengan spasi depan dan belakang tetap terdeteksi

33. Klik `[Clear Field]`
34. Ketik `  finance  ` (2 spasi di depan dan belakang) pada field Division Name, lalu berhenti mengetik ±500 ms
35. Verifikasi error inline `Division Name already exists` muncul

### TC-GS-DIV-42: Submit langsung dengan Division Name duplikat sebelum debounce selesai ditolak

36. Klik `[Clear Field]`
37. Ketik `Finance` pada field Division Name
38. Klik `[Submit]` segera, sebelum 500 ms berlalu sejak ketikan terakhir
39. Tunggu respons check-availability selesai
40. Verifikasi record tidak dibuat: jumlah Division lewat API sama dengan baseline
41. Verifikasi error inline `Division Name already exists` tampil
42. Verifikasi modal tetap terbuka
43. Verifikasi input `Finance` dipertahankan di field Division Name

### Tutup form dirty

44. Klik `✕` untuk menutup form yang masih dirty
45. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
46. Klik `[Leave]` pada dialog `Unsaved Changes`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Seluruh validasi memakai satu pembukaan form (prinsip 3, 6, dan 7 konvensi): validasi diblokir berurutan dalam urutan TC sumber, tiap validasi diakhiri submit yang diblokir, dan form ditutup di akhir spec (langkah 44 sampai 46). Pengecekan jumlah Division terhadap baseline (langkah 5, 10, dan 40) memakai API karena tabel tertutup modal; langkah 40 mencakup juga seluruh submit sebelumnya karena jumlah dibandingkan dengan baseline dari hook `before`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12, 19, 25, 33, dan 36 (`[Clear Field]` mengosongkan field Division Name sebelum nilai uji berikutnya), langkah 39 (menunggu respons check-availability selesai sebelum asersi hasil Submit), serta langkah 44 dan 46 (menutup form dirty lewat `✕` dan `[Leave]`; langkah 45 memverifikasi dialog `Unsaved Changes` sesuai S-08, bukan Expected TC).
- Langkah 17 dan 18 (TC-GS-DIV-38) serta langkah 23 dan 24 (TC-GS-DIV-39) menambahkan submit yang diblokir sesuai prinsip 7 konvensi; TC sumber hanya meminta error inline pada kedua TC itu.
- Spec melewati sekitar 35 langkah (46 langkah) karena tujuh TC validasi Name berkelas harness sama (validasi diblokir), memakai satu akun dan satu pembukaan form; butir Expected bermajemuk dipecah per klausa (S-01). Tiap blok berdiri sendiri (diawali `[Clear Field]` dan memakai nilai sendiri), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pemecahan hanya menambah login, hook, dan pembukaan form.
- Temuan untuk QA:
  - TC-GS-DIV-38 dan TC-GS-DIV-39 tidak memuat langkah submit; langkah 17, 18, 23, dan 24 adalah tambahan prinsip 7 konvensi (bukan Expected TC).
  - TC-GS-DIV-39 menyatakan emoji menampilkan error inline `Division Name contains invalid characters` (karakter masuk ke field), sedangkan suite Brand memfilter emoji di level input; spec mengikuti TC Division.
  - TC-GS-DIV-42 menyebut "segera klik `[Submit]` sebelum 500ms" tanpa menyatakan apakah error inline berasal dari re-check atomik saat Submit atau dari debounce yang selesai; spec hanya mengasersi hasil akhirnya (langkah 40 sampai 43).
