---
id: TC-AUTH-ACT-E2E-014-activation-success-dan-go-to-login
title: "Halaman Activation Success, CTA Go to Login, dan guard akses halaman sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-73
  - TC-AUTH-ACT-74
  - TC-AUTH-ACT-75
  - TC-AUTH-ACT-76
  - TC-AUTH-ACT-77
  - TC-AUTH-ACT-78
coverage:
  web: automated
---

# Halaman Activation Success, CTA Go to Login, dan guard akses halaman sukses

## Prerequisites

- Browser publik tanpa sesi login (utama).
- 6 user seeding milik automation, masing-masing berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run): satu user untuk tiap blok TC-AUTH-ACT-73 s.d. TC-AUTH-ACT-78; hook `after` menghapus user serta menutup sesi.
- Konteks browser terpisah yang sudah memiliki sesi login aktif milik user lain (admin Global Settings), khusus untuk TC-AUTH-ACT-78.
- Akses API read-only untuk memverifikasi status user (Activated) dan token (Consumed), serta memastikan sesi login pada TC-AUTH-ACT-78 tidak berubah.

## Test Steps

### Screening halaman Activation Success (TC-AUTH-ACT-73)

1. Buka link aktivasi user pertama → halaman Set Password tampil.
2. Ketik `Aman#Sandi8` pada field Password dan Confirm Password, lalu klik button "Set Password".
3. Susuri halaman Activation Success dari atas ke bawah tanpa klik apa pun.
4. Verifikasi **Header**: Card (Elevated) single-column di tengah layar dengan ilustrasi sukses (success illustration) di atas.
5. Verifikasi **Body**: Title "Account Activated" dan Body "Your account is now active. You can log in with your new password."
6. Verifikasi **Footer**: CTA "Go to Login" enabled di dalam EmptyState dan tidak ada aksi lain di halaman.

### Klik Go to Login menuju Login with Password (TC-AUTH-ACT-74)

7. Buka link aktivasi user kedua → Set Password → ketik `Aman#Sandi8` di kedua field → klik "Set Password".
8. Pada halaman Activation Success, klik CTA "Go to Login".
9. Verifikasi halaman Login with Password tampil.
10. Verifikasi tidak ada pemeriksaan atau pesan terkait sesi lain pada transisi.

### Reload halaman Activation Success mengarahkan ke Login (TC-AUTH-ACT-75)

11. Buka link aktivasi user ketiga → Set Password → aktivasi dengan `Aman#Sandi8`.
12. Pada halaman Activation Success, reload halaman (F5).
13. Verifikasi halaman Login tampil dan halaman Activation Success tidak tampil kembali.

### Tombol Back browser tidak membuka kembali Activation Success (TC-AUTH-ACT-76)

14. Buka link aktivasi user keempat → Set Password → aktivasi dengan `Aman#Sandi8`.
15. Klik CTA "Go to Login" → halaman Login with Password tampil.
16. Tekan tombol Back browser.
17. Verifikasi halaman Login tampil dan halaman Activation Success tidak tampil kembali.

### Akses langsung URL Activation Success mengarahkan ke Login (TC-AUTH-ACT-77)

18. Buka link aktivasi user kelima → Set Password → aktivasi dengan `Aman#Sandi8`.
19. Salin URL halaman Activation Success dari address bar.
20. Tempel URL tersebut di tab baru dan buka.
21. Verifikasi halaman Login tampil di tab baru dan halaman Activation Success tidak tampil.

### Go to Login dengan sesi login user lain aktif (TC-AUTH-ACT-78)

22. Pada konteks browser yang sudah memiliki sesi login aktif milik admin Global Settings, buka link aktivasi user keenam.
23. Verifikasi halaman Set Password tampil, lalu aktivasi dengan `Aman#Sandi8` di kedua field.
24. Klik CTA "Go to Login".
25. Verifikasi halaman Login with Password selalu tampil.
26. Verifikasi sesi login aktif milik admin tidak diperiksa dan tidak berubah (admin tetap login).

## Notes

- Tiap blok mengonsumsi token user sendiri sehingga urutan blok bebas dari dependensi; screening halaman sukses diletakkan pertama.
- Guard akses halaman sukses (reload, Back, URL langsung) berbagi pola "aktivasi lalu coba akses ulang" sehingga digabung dalam satu spec dengan user berbeda per blok.
- Kebutuhan sesi admin aktif untuk TC-AUTH-ACT-78 dicatat di Prerequisites.
