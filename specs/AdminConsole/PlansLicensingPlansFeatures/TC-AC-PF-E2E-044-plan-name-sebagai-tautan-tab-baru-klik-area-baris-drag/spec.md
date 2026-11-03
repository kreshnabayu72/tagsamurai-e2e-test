---
id: TC-AC-PF-E2E-044-plan-name-sebagai-tautan-tab-baru-klik-area-baris-drag
title: Plan Name sebagai Tautan - Tab Baru, Klik Area Baris, Drag-Select, Keyboard, dan Klik Ganda
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-777
  - TC-AC-PF-778
  - TC-AC-PF-779
  - TC-AC-PF-780
  - TC-AC-PF-782
coverage:
  web: automated
---

# Plan Name sebagai Tautan - Tab Baru, Klik Area Baris, Drag-Select, Keyboard, dan Klik Ganda

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal; password dari env `AC_TC_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan A (default aktif Starter (FAMS, Free, v2), Growth (FAMS, Paid, v5), Professional (FAMS, Paid, v3), Enterprise, SIEM). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: kemampuan membuka dan berpindah antar tab browser, Ctrl+klik, klik tengah, drag mouse, klik ganda, tombol Tab, Shift+Tab, dan tombol Back browser; fixture backend (pemulihan Dataset Pre-setup) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tab browser tambahan yang dibuka langkah 2 dan 6 ditutup di langkah 10; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-PF-777: tautan Plan Name, Ctrl+klik, dan klik tengah

1. Verifikasi teks `Growth` di kolom Plan Name berupa elemen tautan dengan atribut `href` yang menuju halaman Plan Detail `Growth`.
2. Ctrl+klik (Cmd+klik di macOS) teks `Growth`.
3. Verifikasi Plan Detail `Growth` terbuka di tab baru.
4. Kembali ke tab asal.
5. Verifikasi tab asal tetap menampilkan Plans & Licensing > Plans & Features > Default > Active.
6. Klik tengah (middle-click) teks `Growth`.
7. Verifikasi satu tab baru lagi berisi Plan Detail `Growth` terbuka.
8. Kembali ke tab asal.
9. Verifikasi tab asal tetap di list.
10. Tutup kedua tab baru.

### TC-AC-PF-778: klik pada sel baris selain Plan Name

11. Klik sel Product baris `Growth`.
12. Verifikasi halaman tetap di Plans & Licensing > Plans & Features > Default > Active tanpa Plan Detail, form, dialog, atau overlay yang terbuka.
13. Klik sel Clients baris `Growth`.
14. Verifikasi halaman tetap di Plans & Licensing > Plans & Features > Default > Active tanpa Plan Detail, form, dialog, atau overlay yang terbuka.
15. Klik sel Last Modified baris `Growth`.
16. Verifikasi halaman tetap di Plans & Licensing > Plans & Features > Default > Active tanpa Plan Detail, form, dialog, atau overlay yang terbuka.

### TC-AC-PF-779: drag-select Plan Name

17. Tekan tombol mouse pada awal teks `Professional` di kolom Plan Name, geser hingga akhir teks, lalu lepas tombol mouse.
18. Verifikasi teks `Professional` terseleksi.
19. Verifikasi halaman tetap di list dan Plan Detail tidak terbuka.
20. Klik penuh (tekan dan lepas tanpa geser) teks `Professional`.
21. Verifikasi Plan Detail `Professional` terbuka pada tab yang sama.
22. Kembali ke list lewat Breadcrumb.

### TC-AC-PF-780: akses keyboard Plan Name

23. Tekan Tab berulang sampai fokus mendarat pada teks `Starter` di kolom Plan Name baris pertama.
24. Verifikasi tautan `Starter` menerima fokus dengan indikator fokus tampak.
25. Verifikasi nama aksesibel tautan berupa label deskriptif yang memuat `Starter`, bukan teks polos `Starter`.
26. Tekan Tab satu kali.
27. Verifikasi fokus berikutnya berada pada ikon `⋯` row action baris `Starter`.
28. Tekan Shift+Tab untuk kembali ke tautan `Starter`.
29. Tekan Enter.
30. Verifikasi Plan Detail `Starter` terbuka pada tab yang sama.
31. Kembali ke list lewat Breadcrumb.

### TC-AC-PF-782: klik ganda cepat

32. Klik ganda cepat (double-click) teks `Growth` di kolom Plan Name.
33. Verifikasi Plan Detail `Growth` terbuka satu kali tanpa galat dan tanpa pemuatan ganda.
34. Klik tombol Back browser satu kali.
35. Verifikasi halaman kembali ke Plans & Licensing > Plans & Features > Default > Active.

## Notes

- Langkah penghubung (S-03): langkah 4, 8, dan 10 (berpindah tab browser dan menutup tab tambahan), langkah 22 dan 31 (kembali ke list). Langkah 4 dan 8 memenuhi langkah TC "Kembali ke tab asal".
- Temuan untuk QA:
  - TC-AC-PF-777 Expected b dan c tidak menyebut apakah tab baru dari Ctrl+klik dan klik tengah terbuka di latar belakang; spec berpindah ke tab asal dengan "Kembali ke tab asal" sebagai langkah penghubung.
  - TC-AC-PF-782 Expected a ("tanpa galat dan tanpa pemuatan ganda") tidak menyebut cara mengamati galat atau pemuatan ganda; spec menuliskannya apa adanya (langkah 33).
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
