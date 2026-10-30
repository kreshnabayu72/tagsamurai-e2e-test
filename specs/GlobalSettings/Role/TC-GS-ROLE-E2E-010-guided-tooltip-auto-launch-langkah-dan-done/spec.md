---
id: TC-GS-ROLE-E2E-010-guided-tooltip-auto-launch-langkah-dan-done
title: "Guided Tooltip Role & Permission: Kunjungan Pertama, Langkah 1 sampai 3, Done, dan Tab Aktif"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-26
  - TC-GS-ROLE-27
  - TC-GS-ROLE-28
coverage:
  web: automated
---

# Guided Tooltip Role & Permission: Kunjungan Pertama, Langkah 1 sampai 3, Done, dan Tab Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Ahmad Fauzi) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Data: memakai data Pre-setup (Pre-setup #1); spec tidak membuat, mengubah, atau menghapus data.
- Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_gs-role`, sehingga flag dihapus ("belum diset") lewat API sebelum tiap TC (langkah reset eksplisit) dan menjadi pengecualian atas pernyataan hook suite di `suite.md`. Hook `before` spec mencatat nilai awal flag sesudah hook suite menyetelnya; hook `after` memulihkan nilai awal walau spec gagal di tengah.
- Kemampuan teknis: menghapus nilai flag `guided_tooltip_seen_gs-role` akun aktor lewat API (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); muat ulang halaman (F5); membuka URL Role & Permission > System langsung di address bar (URL disediakan tim FE).
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-ROLE-26: Walkthrough otomatis pada kunjungan pertama di Tab Total Control

1. Hapus flag `guided_tooltip_seen_gs-role` lewat API sehingga flag belum diset
2. Buka Global Settings > Role & Permission untuk kunjungan pertama
3. Verifikasi walkthrough mulai dari Step 1 di Tab Total Control
4. Verifikasi Step 1 menyorot Tabs
5. Verifikasi Title Step 1 adalah "Access Level Navigation"
6. Verifikasi Description Step 1 adalah "Switch between access levels and individual roles to configure user permissions."
7. Verifikasi `[Back]` Hidden pada Step 1

### TC-GS-ROLE-27: Step 2 dan Step 3 lalu Done

8. Hapus flag `guided_tooltip_seen_gs-role` lewat API sehingga flag belum diset
9. Muat ulang Global Settings > Role & Permission untuk kunjungan pertama
10. Klik `[Next]` ke Step 2
11. Verifikasi Step 2 menyorot ikon Search Tab Total Control
12. Verifikasi Title Step 2 adalah "Search"
13. Verifikasi Description Step 2 adalah "Quickly search by name to find a specific entry. What you can search depends on the tab you are on."
14. Klik `[Next]` ke Step 3
15. Verifikasi Step 3 menyorot header kolom Actions `[⋯]`
16. Verifikasi Title Step 3 adalah "Table Actions"
17. Verifikasi Description Step 3 adalah "Manage which columns are shown from the header actions menu, and use the row action menu for actions on each row. Available actions depend on the tab you are on."
18. Verifikasi pada Step 3 tombol `[Next]` berubah menjadi `[Done]`
19. Klik `[Done]`
20. Verifikasi `[Done]` menutup walkthrough
21. Muat ulang halaman (F5)
22. Verifikasi walkthrough tidak muncul otomatis

### TC-GS-ROLE-28: Walkthrough dimulai di tab yang sedang aktif tanpa berpindah tab

23. Hapus flag `guided_tooltip_seen_gs-role` lewat API sehingga flag belum diset
24. Buka URL Role & Permission > System langsung di address bar
25. Verifikasi halaman terbuka di Tab System
26. Verifikasi walkthrough mulai dari Step 1 di Tab System (tidak dialihkan ke Tab Total Control)
27. Verifikasi Tab System tetap aktif
28. Verifikasi Breadcrumb tetap "Role & Permission > System"
29. Klik `[Next]` ke Step 2
30. Verifikasi Step 2 menyorot ikon Search Tab System
31. Verifikasi placeholder pencarian Tab System adalah "Search role..."
32. Verifikasi Tab System tetap aktif
33. Verifikasi Breadcrumb tetap "Role & Permission > System"
34. Klik `[Next]` ke Step 3
35. Verifikasi Step 3 menyorot header kolom Actions `[⋯]` Tab System
36. Verifikasi Tab System tetap aktif
37. Verifikasi Breadcrumb tetap "Role & Permission > System"
38. Verifikasi tidak ada route navigation selama walkthrough
39. Verifikasi tidak ada dialog otomatis selama walkthrough
40. Klik `[Done]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (40 langkah) karena tiga TC berada di satu kelas harness (fungsional, state flag Guided Tooltip akun aktor); tiap blok TC mereset flag di awalnya (langkah 1, 8, 23) sehingga berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 8, dan 23 (hapus flag lewat API untuk memenuhi precondition "flag belum diset"), langkah 9 (muat ulang agar kunjungan pertama berikutnya terpenuhi), dan langkah 40 (`[Done]` menutup walkthrough Tab System; TC-GS-ROLE-28 langkah 4).
- Langkah 27, 28, 32, 33, 36, dan 37 menjalankan TC-GS-ROLE-28 langkah 3 ("amati tab aktif dan breadcrumb di tiap step") dan Expected d; Step 1 (langkah 27 dan 28) ikut diamati.
- Temuan untuk QA:
  - TC-GS-ROLE-26 menyebut flag `gs-role-permission`, sedangkan `suite.md` dan konvensi hook memakai `guided_tooltip_seen_gs-role`; spec memakai nama dari `suite.md`.
  - TC-GS-ROLE-28 tidak memberi URL literal Role & Permission > System; spec memakai URL yang disediakan tim FE.
  - TC-GS-ROLE-28 Expected b menyebut placeholder "Search role..." pada Step 2 padahal Step 2 menyorot ikon Search (input belum dibuka); spec mengasersi placeholder sesuai TC dan perlu dipastikan QA apakah placeholder terlihat pada saat Step 2.
  - TC-GS-ROLE-28 Expected a hanya menyebut posisi Step 1 di Tab System; Title dan Description Step 1 Tab System tidak diasersi.
