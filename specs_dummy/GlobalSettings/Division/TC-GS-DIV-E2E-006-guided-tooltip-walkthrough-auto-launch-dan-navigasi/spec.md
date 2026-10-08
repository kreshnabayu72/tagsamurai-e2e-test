---
id: TC-GS-DIV-E2E-006-guided-tooltip-walkthrough-auto-launch-dan-navigasi
title: "Guided Tooltip Walkthrough 3-Langkah: Auto-Launch Kunjungan Pertama, Kontrol Navigasi, Overlay Dismiss, dan Replay"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-10
  - TC-GS-DIV-11
  - TC-GS-DIV-12
  - TC-GS-DIV-13
  - TC-GS-DIV-14
coverage:
  web: automated
---

# Guided Tooltip Walkthrough 3-Langkah: Auto-Launch Kunjungan Pertama, Kontrol Navigasi, Overlay Dismiss, dan Replay

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Flag guided_tooltip_seen_gs-division belum ada untuk akun uji (kunjungan pertama)
- Akun uji: Total Control
- Flag `guided_tooltip_seen_gs-division` belum ada untuk akun ini
- User berada di Global Settings > User > Division
- Flag `guided_tooltip_seen_gs-division` sudah true

## Test Steps

### Konten 3 step Guided Tooltip halaman Division sesuai urutan (TC-GS-DIV-10)

1. Buka Global Settings > User > Tab Division untuk kunjungan pertama
2. Baca Step 1
3. Klik `[Next]` dan baca Step 2
4. Klik `[Next]` dan baca Step 3
5. Verifikasi Step 1: target Tombol `[+ Division]`, Title `Add Division`, Description `Create a new division to group the staff accounts in your organization.`
6. Verifikasi Step 2: target Tabel Division List (T-DIV-01), Title `Division Table`, Description `Browse and manage all divisions in your organization from this table.`
7. Verifikasi Step 3: target Icon `[Changelog]`, Title `Changelog Audit`, Description `Review the history of changes made to divisions.`

### Walkthrough otomatis pada kunjungan pertama dan tidak muncul lagi setelah Skip (TC-GS-DIV-11)

8. Buka Tab Division untuk kunjungan pertama
9. Klik `[Skip]`
10. Muat ulang halaman (F5)
11. Verifikasi Walkthrough muncul otomatis dari Step 1 pada kunjungan pertama
12. Verifikasi Klik `[Skip]` menutup walkthrough dan menyimpan flag `seen`
13. Verifikasi Setelah F5 walkthrough tidak muncul otomatis lagi

### Klik overlay gelap menutup walkthrough dan menyimpan flag seen (TC-GS-DIV-12)

14. Buka Tab Division untuk kunjungan pertama
15. Klik area overlay gelap di luar tooltip
16. Muat ulang halaman (F5)
17. Verifikasi Klik overlay menutup walkthrough
18. Verifikasi Flag `seen` tersimpan sehingga walkthrough tidak muncul lagi setelah F5

### Navigasi Back, Next, dan Done pada walkthrough (TC-GS-DIV-13)

19. Buka Tab Division untuk kunjungan pertama
20. Perhatikan tombol di Step 1
21. Klik `[Next]` ke Step 2
22. Klik `[Back]`
23. Klik `[Next]` dua kali sampai Step 3
24. Perhatikan label tombol primer, lalu klik tombol itu
25. Verifikasi Step 1: tombol `[Back]` Hidden
26. Verifikasi Step 2 muncul setelah Next, `[Back]` kembali ke Step 1
27. Verifikasi Step 3 (terakhir): `[Next]` berubah menjadi `[Done]`
28. Verifikasi Klik `[Done]` menutup walkthrough dan menyimpan flag `seen`

### Tombol [?] memulai ulang walkthrough dari Step 1 tanpa mereset flag (TC-GS-DIV-14)

29. Klik trigger `[?]` di header halaman
30. Klik `[Skip]`
31. Muat ulang halaman (F5)
32. Verifikasi Walkthrough mulai dari Step 1
33. Verifikasi Flag `seen` tetap true (tidak di-reset) sehingga setelah F5 walkthrough tidak muncul otomatis

## Notes

- Memvalidasi peluncuran otomatis tur terpandu 3-langkah (Step 1: [+ Division], Step 2: Division Table, Step 3: Changelog), tombol Next/Back/Done, tombol Skip, penutupan via klik overlay gelap, penyimpanan flag seen, dan pemutaran ulang tur via tombol help [?] (PRD §4.7).
- Sumber pemetaan test case granular: TC-GS-DIV-10, TC-GS-DIV-11, TC-GS-DIV-12, TC-GS-DIV-13, TC-GS-DIV-14.
