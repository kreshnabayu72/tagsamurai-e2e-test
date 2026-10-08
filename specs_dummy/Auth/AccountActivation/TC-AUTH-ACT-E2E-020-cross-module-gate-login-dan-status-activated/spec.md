---
id: TC-AUTH-ACT-E2E-020-cross-module-gate-login-dan-status-activated
title: "Lintas modul: penolakan login belum aktivasi, refleksi status Activated, dan siklus toggle pasca-aktivasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-98
  - TC-AUTH-ACT-106
  - TC-AUTH-ACT-107
  - TC-AUTH-ACT-108
  - TC-AUTH-ACT-109
coverage:
  web: automated
---

# Lintas modul: penolakan login belum aktivasi, refleksi status Activated, dan siklus toggle pasca-aktivasi

## Prerequisites

- Jendela privat tanpa sesi login untuk alur aktivasi dan percobaan login.
- Sesi login Role: Total Control (Global Settings) di browser admin, untuk memeriksa Activity Log dan `Global Settings > User`.
- Kemampuan menyelesaikan reCAPTCHA pada form login (test key otomatis lolos) dan memantau request jaringan untuk memastikan login tidak diproses.
- 5 user seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run): user untuk blok TC-AUTH-ACT-107, 98, 106, 108, dan 109; user blok 108 dan 109 diaktivasi di dalam spec; hook `after` membersihkan seluruh user.
- Akses API read-only untuk memverifikasi status user sebelum serta sesudah tiap aktivasi.

## Test Steps

### User belum aktivasi ditolak login (TC-AUTH-ACT-107)

1. Buka `Auth > Login > Login with Password` di jendela privat.
2. Isi Email user blok 107 dan Password `Aman#Sandi8`, selesaikan reCAPTCHA, lalu klik [Log in].
3. Verifikasi pesan "Your account has not been activated" tampil dan login tidak diproses.
4. Verifikasi halaman tetap `Auth > Login > Login with Password`.
5. Verifikasi via API bahwa status user tetap Pending Activation.

### Penolakan login dicatat oleh modul Login (TC-AUTH-ACT-98)

6. Di jendela privat, isi Email user blok 98 dan Password `Aman#Sandi8` pada Login with Password, selesaikan reCAPTCHA, lalu klik [Log in].
7. Verifikasi pesan "Your account has not been activated" tampil.
8. Pada browser admin, buka `Global Settings > Activity Log > Session` dan cari entri untuk email user blok 98.
9. Verifikasi Activity Log (Session) memuat entri Failed dengan Note `Account is not activated` yang berasal dari modul Login.
10. Verifikasi tidak ada entri bertanda aktivasi atau Set Password dari Auth Account Activation untuk user tersebut.

### Aktivasi merefleksikan status Activated di Global Settings > User (TC-AUTH-ACT-106)

11. Buka link aktivasi user blok 106 → halaman Set Password tampil.
12. Ketik `Aman#Sandi8` pada kedua field, lalu klik button "Set Password".
13. Verifikasi halaman Activation Success tampil.
14. Pada browser admin, muat ulang `Global Settings > User > Login User` dan cari user blok 106.
15. Verifikasi user tidak lagi berbadge Pending Activation pada tabel.
16. Buka `Global Settings > User > Detail` untuk user tersebut.
17. Verifikasi Status Badge pada Detail tidak lagi menampilkan Pending Activation.

### Setelah aktivasi, login tidak lagi ditolak (TC-AUTH-ACT-108)

18. Buka link aktivasi user blok 108 → Set Password → ketik `Aman#Sandi8` pada kedua field → klik button "Set Password" sampai Activation Success tampil.
19. Buka `Auth > Login > Login with Password` di jendela privat.
20. Isi Email user blok 108 dan Password `Aman#Sandi8` (password yang ditetapkan saat aktivasi), selesaikan reCAPTCHA, lalu klik [Log in].
21. Verifikasi pesan "Your account has not been activated" tidak tampil.
22. Verifikasi kredensial diterima: form kredensial Login with Password tidak ditampilkan lagi dan alur berlanjut ke tahap berikutnya milik modul Login (perilaku lanjutan di-assert pada TC modul Login).

### Siklus Deactivate/Activate tidak mengembalikan status Pending (TC-AUTH-ACT-109)

23. Buka link aktivasi user blok 109 → Set Password → aktivasi dengan `Aman#Sandi8` sampai Activation Success tampil.
24. Pada browser admin di `Global Settings > User > Login User`, matikan toggle Active user blok 109, lalu klik [Deactivate] pada dialog konfirmasi.
25. Nyalakan kembali toggle Active, lalu klik [Activate] pada dialog konfirmasi.
26. Muat ulang `Global Settings > User > Login User` dan cari user tersebut.
27. Verifikasi user tidak berbadge Pending Activation (status Activation tetap Activated).
28. Buka kembali link aktivasi user tersebut.
29. Verifikasi halaman Invalid Link varian Used tampil (token tetap Consumed).

## Notes

- Urutan: screening penolakan login (belum ada data berubah) → aktivasi dan verifikasi status → login sukses → siklus toggle pasca-aktivasi sebagai penutup.
- Kebutuhan reCAPTCHA, dua sesi browser, dan akses Activity Log dicatat di Prerequisites.
