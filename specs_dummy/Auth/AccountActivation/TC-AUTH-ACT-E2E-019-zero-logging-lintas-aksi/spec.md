---
id: TC-AUTH-ACT-E2E-019-zero-logging-lintas-aksi
title: "Zero-logging: membuka link, Set Password, Go to Login, Resend, dan pembuatan user tidak mencatat entri Auth"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-90
  - TC-AUTH-ACT-91
  - TC-AUTH-ACT-92
  - TC-AUTH-ACT-93
  - TC-AUTH-ACT-94
  - TC-AUTH-ACT-95
  - TC-AUTH-ACT-96
  - TC-AUTH-ACT-97
coverage:
  web: automated
---

# Zero-logging: membuka link, Set Password, Go to Login, Resend, dan pembuatan user tidak mencatat entri Auth

## Prerequisites

- Sesi login Role: Total Control (Global Settings) di browser admin, untuk membuka keempat surface log.
- Jendela privat tanpa sesi login, untuk menjalankan seluruh aksi aktivasi.
- Empat surface log yang dibuka dan diperiksa tiap blok: Activity Log (`Global Settings > Activity Log > Session`), serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` target user; jangkar: entri pembuatan user oleh admin tetap terlihat sebagai pembanding.
- 7 user seeding milik automation, dibuat lewat API di hook `before` (email unik per run) berstatus Pending Activation dengan token Active, untuk blok TC-AUTH-ACT-90, 91, 92, 93, 94, 95, dan 97; satu user lagi dibuat langsung lewat popup Create User oleh admin pada blok TC-AUTH-ACT-96; hook `after` membersihkan seluruh user.
- Akses API read-only untuk memverifikasi status token/user, termasuk konversi token user TC-AUTH-ACT-95 menjadi Consumed sebelum kasusnya.

## Test Steps

### Membuka link valid tidak menulis pencatatan (TC-AUTH-ACT-90)

1. Untuk user blok 90, catat jumlah entri pada keempat surface log di browser admin.
2. Di jendela privat, buka link aktivasi user tersebut → halaman Set Password tampil.
3. Muat ulang keempat surface dan bandingkan jumlah entri untuk user tersebut.
4. Verifikasi tidak ada entri baru pada Activity Log (Session), User Log, System Log, dan Changelog akibat pembukaan link valid.
5. Verifikasi entri jangkar milik modul lain tetap tampil dengan jumlah tidak berubah.

### Membuka link tidak valid tidak menulis pencatatan (TC-AUTH-ACT-91)

6. Untuk user blok 91, catat jumlah entri pada keempat surface.
7. Di jendela privat, buka link aktivasi dengan token `unknown-token-12345` → halaman Invalid Link tampil.
8. Muat ulang keempat surface dan bandingkan jumlah entri.
9. Verifikasi tidak ada entri baru pada keempat surface akibat pembukaan link tidak valid dan tampilnya halaman 404.
10. Verifikasi entri jangkar tetap tampil dan jumlahnya tidak berubah.

### Set Password gagal validasi tidak menulis pencatatan (TC-AUTH-ACT-93)

11. Untuk user blok 93, catat jumlah entri pada keempat surface.
12. Di jendela privat, buka link aktivasi user tersebut, klik button "Set Password" dengan kedua field kosong, lalu ketik `abc` pada Password dan `abc` pada Confirm Password dan klik button "Set Password" lagi.
13. Muat ulang keempat surface dan bandingkan jumlah entri.
14. Verifikasi tidak ada entri baru pada keempat surface akibat percobaan Set Password yang gagal validasi.
15. Verifikasi entri jangkar tetap tampil dan jumlahnya tidak berubah.

### Pembuatan user dan pengiriman Activation Email tidak menambah entri dari Auth (TC-AUTH-ACT-96)

16. Buka `Global Settings > User > Login User > Popup Create User` sebagai admin, buat user baru dengan Name `Rina Puspita` dan email unik per run, lalu klik [Submit].
17. Buka Activity Log serta Tab Changelog, Tab System Log, dan Tab User Log pada Detail user tersebut.
18. Verifikasi Changelog dan surface log Global Settings > User memuat entri pembuatan user milik modul Global Settings > User (jangkar).
19. Verifikasi tidak ada entri dari Auth yang mencatat pembuatan token aktivasi atau pengiriman Activation Email pada keempat surface.

### Resend Activation Email tidak menambah entri dari Auth (TC-AUTH-ACT-97)

20. Untuk user blok 97, lakukan Resend Activation Email dari `Global Settings > User > Login User`.
21. Buka keempat surface log untuk user tersebut.
22. Verifikasi hanya entri Resend Activation Email milik modul pemicu (Global Settings > User) yang muncul.
23. Verifikasi tidak ada entri token superseded atau invalidated dari Auth pada Activity Log (Session), User Log, System Log, maupun Changelog.
24. Verifikasi via API bahwa token lama berstatus Superseded dan token baru Active.

### Set Password berhasil tidak menulis pencatatan (TC-AUTH-ACT-92)

25. Untuk user blok 92, catat jumlah entri pada keempat surface.
26. Di jendela privat, buka link aktivasi user tersebut, ketik `Aman#Sandi8` pada kedua field, lalu klik button "Set Password".
27. Muat ulang keempat surface dan bandingkan jumlah entri.
28. Verifikasi tidak ada entri baru pada keempat surface akibat aktivasi berhasil (token consumed dan transisi status).
29. Verifikasi entri jangkar tetap tampil dan jumlahnya tidak berubah.

### Klik Go to Login tidak menulis pencatatan (TC-AUTH-ACT-94)

30. Untuk user blok 94, catat jumlah entri pada keempat surface.
31. Di jendela privat, aktivasi user tersebut (`Aman#Sandi8` di kedua field), lalu pada halaman Activation Success klik CTA "Go to Login".
32. Muat ulang keempat surface dan bandingkan jumlah entri.
33. Verifikasi tidak ada entri baru pada keempat surface akibat klik Go to Login.
34. Verifikasi entri jangkar tetap tampil dan jumlahnya tidak berubah.

### Membuka link terpakai (varian Used) tidak menulis pencatatan (TC-AUTH-ACT-95)

35. Untuk user blok 95, aktivasi user tersebut terlebih dahulu, lalu catat jumlah entri pada keempat surface.
36. Di jendela privat, buka kembali link aktivasi user tersebut yang sudah dipakai → halaman Invalid Link varian Used tampil.
37. Muat ulang keempat surface dan bandingkan jumlah entri.
38. Verifikasi tidak ada entri baru pada keempat surface akibat tampilnya halaman 404 varian Used.
39. Verifikasi entri jangkar tetap tampil dan jumlahnya tidak berubah.

## Notes

- Semua kasus berbagi pola yang sama (catat jangkar → jalankan aksi → muat ulang → bandingkan), sehingga digabung dalam satu spec dengan satu user per blok agar kegagalan tertelusur ke TC yang tepat.
- Blok yang mengonsumsi token (92, 94, 95) diletakkan terakhir; TC-AUTH-ACT-95 mengaktivasi user miliknya sendiri sebelum memeriksa varian Used.
- Kebutuhan dua sesi browser dan keempat surface log dicatat di Prerequisites.
