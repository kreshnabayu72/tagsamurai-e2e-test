---
id: TC-AC-LA-E2E-009-screening-modal-allocation-log
title: "Screening Modal Allocation Log: Isi, Copy ID, Scroll, Empty State, dan Cara Tutup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-39
  - TC-AC-LA-40
  - TC-AC-LA-41
  - TC-AC-LA-42
  - TC-AC-LA-43
coverage:
  web: automated
---

# Screening Modal Allocation Log: Isi, Copy ID, Scroll, Empty State, dan Cara Tutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini kecuali dinyatakan lain; data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data Pre-setup yang dibaca: #55 alokasi dengan riwayat log lengkap (12 entri; created, edited berkali-kali, approved, activated, expired) dan #60 alokasi `Waiting for Approval` Concurrent User +5 requester `Sari P` dengan Payment `Free`. Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seed55, seed60).
- Kemampuan teknis: baca isi clipboard (disediakan tim FE); jeda nyata 3 detik pada TC-AC-LA-40 (di bawah 30 detik, disebut eksplisit).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-39: Screening modal Allocation Log

1. Ketik Search Allocation ID seed riwayat lengkap (`Fixture.license-allocation-license.seed55`), tekan Enter
2. Klik ikon `⋯` pada baris itu, lalu klik row action `Allocation Log`
3. Amati Zona 1, Zona 2, dan Zona 3 modal
4. Verifikasi Header: judul `Allocation Log` diikuti Allocation ID dan ikon Copy di kanan ID
5. Verifikasi Header: `Status:` badge status record saat ini
6. Verifikasi Header: `Client:` nama client
7. Verifikasi Header: `Paid From:` nama entitas sumber kantong
8. Verifikasi Body: daftar kronologis terbaru di atas, tiap entri berisi baris judul dan Date & Time, lalu baris Description bila event punya isi
9. Verifikasi Body: tanpa toolbar (tidak ada Search, Filter, Sort, Setup Column, Download) dan tanpa paginasi
10. Verifikasi Footer: tidak ada footer dan tidak ada tombol `[Close]`
11. Verifikasi modal dapat ditutup lewat `[✕]` (tombol `[✕]` tampil di header)

### TC-AC-LA-40: Copy Allocation ID dari header modal

12. Catat jumlah entri Allocation Log sebagai baseline
13. Hover ikon Copy
14. Verifikasi tooltip `Copy to clipboard`
15. Klik ikon Copy
16. Verifikasi Allocation ID tersalin ke clipboard
17. Verifikasi tooltip inline `Copied to clipboard` tampil (bukan toast)
18. Tunggu 3 detik
19. Verifikasi tooltip inline `Copied to clipboard` hilang
20. Verifikasi jumlah entri Allocation Log sama dengan baseline (penyalinan tidak menambah entri log)

### TC-AC-LA-41: Entri terbaru di atas dengan scroll vertikal

21. Verifikasi entri terbaru berada di paling atas daftar
22. Scroll daftar log ke bawah
23. Verifikasi entri `Allocation created` berada di paling bawah
24. Verifikasi hanya daftar log yang di-scroll sedangkan header modal tetap di atas
25. Verifikasi tidak ada kontrol paginasi

### TC-AC-LA-43: Penutupan modal lewat tombol silang dan Esc, bukan klik backdrop

26. Klik area backdrop di luar modal
27. Verifikasi modal tidak tertutup
28. Klik `[×]`
29. Verifikasi modal tertutup
30. Klik ikon `⋯` pada baris itu, lalu klik row action `Allocation Log`
31. Tekan `Esc`
32. Verifikasi modal tertutup

### TC-AC-LA-42: Modal Allocation Log tanpa empty state dan Paid From dash untuk Payment Free

33. Ganti isi kotak search dengan Allocation ID seed `Sari P` Payment `Free` (`Fixture.license-allocation-license.seed60`), tekan Enter
34. Klik ikon `⋯` pada baris itu, lalu klik row action `Allocation Log`
35. Verifikasi daftar berisi minimal satu entri `Allocation created by Sari P`
36. Verifikasi `Paid From:` menampilkan `—`
37. Verifikasi tidak ada empty state pada modal
38. Tutup modal dengan `[×]`
39. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah membuka row action `Allocation Log`, langkah `Amati`, langkah `Tunggu 3 detik`, dan langkah menutup modal. TC-AC-LA-43 dijalankan sebelum TC-AC-LA-42 supaya modal riwayat lengkap (#55) tetap terbuka untuk TC-AC-LA-39 sampai TC-AC-LA-41 dan penutupan modal diuji sekali; reopen modal dengan row action `Allocation Log` sesudah `[×]` (S-10).
- TC-AC-LA-40, TC-AC-LA-41, dan TC-AC-LA-43 bergantung pada TC-AC-LA-39 (modal Allocation Log terbuka); modal itu tidak ditutup sampai TC-AC-LA-43, sehingga langkah pembukaan TC-AC-LA-39 menjadi langkah dependensi bersama (S-04).
- Spec ini di atas 35 langkah. Alasannya: semua blok satu topik (modal Allocation Log) dan satu dataset seed baca-saja, dengan modal yang sama dipakai berurutan oleh TC-AC-LA-39, TC-AC-LA-40, TC-AC-LA-41, dan TC-AC-LA-43.
- Temuan untuk QA:
  - TC-AC-LA-40 Expected d (`Penyalinan tidak menambah entri log`) tidak memberi baseline; spec mencatat jumlah entri sebelum penyalinan.
  - TC-AC-LA-40 Expected b menyebut `tooltip inline Copied to clipboard tampil selama 2 detik`; spec mengasersi tampil sesudah klik dan hilang setelah jeda 3 detik, tanpa mengukur 2 detik.
  - TC-AC-LA-39, TC-AC-LA-41, dan TC-AC-LA-43 tidak menyebut Allocation ID seed #55; identitas dibaca dari fixture.
  - TC-AC-LA-42 Expected a (`minimal satu entri`) tidak menyebut Allocation ID seed #60; identitas dibaca dari fixture.
  - TC-AC-LA-39 Expected c menyebut modal ditutup lewat `[✕]` atau `Esc` pada Footer; asersi penutupan dilakukan di TC-AC-LA-43.
