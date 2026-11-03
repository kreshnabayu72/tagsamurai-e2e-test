---
id: TC-AC-PF-E2E-218-resilience-archive-dan-delete-5xx-dan-tanpa-respons
title: "Resilience: Archive dan Delete Gagal 5xx dan Tanpa Respons pada Custom Plan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-255
  - TC-AC-PF-262
  - TC-AC-PF-722
  - TC-AC-PF-723
coverage:
  web: automated
---

# Resilience: Archive dan Delete Gagal 5xx dan Tanpa Respons pada Custom Plan

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; TC mengasersi state backend).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: b fault injection / resilience.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan G (Pre-setup #27; custom plan `Paket Tanpa Client` dengan 0 subscription, Active) dan Dataset Plan C (Pre-setup #23; custom plan archived `Arsip Custom Satu` v1, Clients 0, tidak pernah dipakai).
- Pengecualian S-06/S-12 butir A-14: `Paket Tanpa Client` dan `Arsip Custom Satu` Pre-setup literal tanpa suffix menjadi target Archive dan Delete yang digagalkan intercept; spec tidak mengubah data itu karena seluruh request gagal. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): `Spectra.intercept` parsial atas respons Archive dan Delete (endpoint diidentifikasi tim FE; tidak tercantum di sumber TC): (a) respons server error 5xx dan (b) respons tidak pernah diterima FE. Intercept dilepas segera setelah pemicu (S-09). Fixture BE untuk membaca status plan dan memulihkan Dataset; sesi API aktor.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-255: Archive gagal 5xx: dialog tetap terbuka dengan toast error dan plan tetap Active

1. Klik tab Custom
2. Ketik Search `Paket Tanpa Client`, tekan Enter
3. Buka Overlay Row Action `Paket Tanpa Client` → klik `Archive`
4. Pasang intercept: respons Archive dijawab server error
5. Klik `[Archive]`
6. Lepas intercept
7. Verifikasi toast error: "Error, failed to archive plan."
8. Verifikasi dialog `Archive Plan` tetap terbuka
9. Verifikasi tombol `[Archive]` aktif kembali untuk retry manual
10. Verifikasi (dibaca lewat fixture BE) `Paket Tanpa Client` tetap Active

### TC-AC-PF-722: Archive tanpa respons (timeout atau jaringan terputus): toast Connection problem, dialog tetap terbuka

11. Dismiss toast error
12. Pasang intercept: respons Archive tidak pernah diterima FE
13. Klik `[Archive]` dan tunggu sampai FE menampilkan kegagalan
14. Lepas intercept
15. Verifikasi muncul toast error: "Connection problem. Please try again."
16. Verifikasi dialog `Archive Plan` tetap terbuka
17. Verifikasi tombol `[Archive]` aktif kembali untuk retry manual
18. Klik `[Cancel]` pada dialog `Archive Plan`
19. Klik `(←)` pada kotak Search

### TC-AC-PF-262: Delete gagal 5xx: dialog tetap terbuka dengan toast error dan plan tetap ada

20. Klik sub-tab Archive
21. Ketik Search `Arsip Custom Satu`, tekan Enter
22. Buka Overlay Row Action `Arsip Custom Satu` → klik `Delete`
23. Pasang intercept: respons Delete dijawab server error
24. Klik `[Delete]`
25. Lepas intercept
26. Verifikasi toast error: "Error, failed to delete plan."
27. Verifikasi dialog `Delete Plan` tetap terbuka
28. Verifikasi tombol `[Delete]` aktif kembali
29. Verifikasi (dibaca lewat fixture BE) `Arsip Custom Satu` tetap ada di sub-tab Archive

### TC-AC-PF-723: Delete tanpa respons (timeout atau jaringan terputus): toast Connection problem, dialog tetap terbuka

30. Dismiss toast error
31. Pasang intercept: respons Delete tidak pernah diterima FE
32. Klik `[Delete]` dan tunggu sampai FE menampilkan kegagalan
33. Lepas intercept
34. Verifikasi muncul toast error: "Connection problem. Please try again."
35. Verifikasi dialog `Delete Plan` tetap terbuka
36. Verifikasi tombol `[Delete]` aktif kembali untuk retry manual
37. Klik `[Cancel]` pada dialog `Delete Plan`
38. Klik `(←)` pada kotak Search

## Notes

- Alasan di atas sekitar 35 langkah (38 langkah): keempat blok satu kelas harness (b, kegagalan atau tanpa respons yang dipaksakan pada dialog konfirmasi), berdiri sendiri pada plan masing-masing, dan tiap pasangan blok (5xx lalu tanpa respons) memakai dialog yang sama sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemecahan lebih lanjut menambah login, hook, dan pembukaan dialog per spec.
- Penyimpangan urutan (S-10): tidak ada; urutan Archive lalu Delete mengikuti topik aksi dan tiap pasangan memakai dialog yang sama sehingga TC tanpa respons mengikuti TC 5xx.
- Langkah penghubung (S-03): langkah 1 dan 20 mengarahkan layar ke tab Custom dan sub-tab Archive; langkah 2 dan 21 menemukan baris target (R-16); langkah 11 dan 30 meng-dismiss toast error agar asersi toast berikutnya bukan toast lama (R-12); langkah 18 dan 37 menutup dialog; langkah 19 dan 38 mengosongkan Search.
- Langkah 10 dan 29 membaca status plan lewat fixture BE (state data) karena dialog masih terbuka dan Expected menyatakan plan tetap pada statusnya.
- Temuan untuk QA:
  - TC-AC-PF-722 dan TC-AC-PF-723: Expected tidak menyebut apakah request sempat diproses server; spec tidak mengasersi status plan pada skenario tanpa respons.
