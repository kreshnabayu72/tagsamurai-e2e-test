---
id: TC-GS-GSET-E2E-009-guided-tooltip-konten-step-dan-navigasi
title: "Guided Tooltip konten dan navigasi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-15
  - TC-GS-GSET-16
  - TC-GS-GSET-18
coverage:
  web: automated
---

# Guided Tooltip konten dan navigasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Budi Santoso, Pre-setup No 1) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Pre-setup No 8 menyebut Total Control baru yang belum pernah membuka General Settings; email akun itu tidak tertulis di Pre-setup TC, sehingga spec memakai akun No 1 dengan flag `seen` dihapus.
- Guided Tooltip: spec ini mengecualikan hook suite untuk flag `guided_tooltip_seen_gs-general-settings` (page_key `gs-general-settings`, PRD §4.7). Hook `before` mencatat nilai awal flag akun aktor dan hook `after` memulihkannya walau spec gagal di tengah. Flag dihapus ("belum ada") oleh langkah eksplisit sebelum tiap TC yang mensyaratkannya. Kemampuan menghapus dan membaca flag akun aktor lewat API disediakan tim FE/BE (nama endpoint tidak disebut di TC, PRD, atau LLD).
- Data Pre-setup No 10 (record Client A, hanya dibaca). Spec tidak menekan `[Save]`.
- Kemampuan teknis: operasi keyboard (`→`, `Enter`, `←`, `Esc`) saat walkthrough aktif; muat ulang halaman (F5).
- State global yang diubah: hanya flag Guided Tooltip akun aktor (dipulihkan seperti di atas).

## Test Steps

### TC-GS-GSET-15: Konten tiap step

1. Hapus flag `guided_tooltip_seen_gs-general-settings` akun aktor lewat API sehingga flag belum ada
2. Muat ulang halaman Global Settings > General Settings (F5) untuk kunjungan pertama
3. Verifikasi walkthrough Step 1 tampil dengan target field Currency Code
4. Verifikasi title Step 1 "Set Your Regional Format"
5. Verifikasi description Step 1 "Currency, time zone, and date/time format set here apply across every product — no need to configure them again per module."
6. Verifikasi tombol `[Back]` Hidden pada Step 1
7. Verifikasi tombol `[Next]` tampil pada Step 1
8. Klik `[Next]`
9. Verifikasi walkthrough Step 2 tampil dengan target field Session Idle Timeout
10. Verifikasi title Step 2 "Control Session Timeout"
11. Verifikasi description Step 2 "Choose how long a user can stay idle before they're automatically logged out."
12. Verifikasi tombol `[Back]` tampil pada Step 2
13. Verifikasi tombol `[Next]` berubah menjadi `[Done]` pada Step 2

### TC-GS-GSET-16: Back, Done, dan replay lewat tombol ?

14. Klik `[Back]`
15. Verifikasi walkthrough kembali ke Step 1
16. Klik `[Next]`
17. Klik `[Done]`
18. Verifikasi walkthrough tertutup
19. Verifikasi flag `guided_tooltip_seen_gs-general-settings` tersimpan (true, dibaca lewat API)
20. Klik tombol `[?]` di header halaman
21. Verifikasi walkthrough dimulai ulang dari Step 1
22. Verifikasi flag `guided_tooltip_seen_gs-general-settings` tetap tersimpan (true, dibaca lewat API; tidak direset)

### TC-GS-GSET-18: Keyboard Esc, Enter, panah kanan, panah kiri

23. Klik `[Skip]` untuk menutup walkthrough hasil replay
24. Hapus flag `guided_tooltip_seen_gs-general-settings` akun aktor lewat API sehingga flag belum ada
25. Muat ulang halaman Global Settings > General Settings (F5)
26. Verifikasi Tooltip box walkthrough Step 1 mendapat fokus keyboard
27. Tekan `→`
28. Verifikasi walkthrough pindah ke Step 2
29. Tekan `←`
30. Verifikasi walkthrough kembali ke Step 1
31. Tekan `Enter`
32. Verifikasi walkthrough pindah ke Step 2
33. Tekan `Esc`
34. Verifikasi walkthrough tertutup
35. Verifikasi flag `guided_tooltip_seen_gs-general-settings` tersimpan (true, dibaca lewat API; setara Skip)

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. 35 langkah, tepat pada batas sekitar 35 langkah; satu kelas (Guided Tooltip), dan tiga blok berdiri sendiri karena flag dihapus ulang di awal blok TC-GS-GSET-18.
- Dipisah dari spec 010 karena gabungan langkahnya melewati batas ukuran jauh (35 + 36 = 71 langkah, tanpa langkah berulang sehingga ekspansi sama); spec ini memuat TC-GS-GSET-15, 16, dan 18 (konten, navigasi, dan keyboard walkthrough), spec 010 memuat TC-GS-GSET-14, 17, 146, dan 147 (trigger kunjungan pertama dan penutupan tanpa menyimpan flag).
- Pecahan Expected: TC-GS-GSET-15 a menjadi langkah 3 sampai 7, b menjadi langkah 9 sampai 13; TC-GS-GSET-16 a menjadi langkah 15, b menjadi langkah 18 dan 19, c menjadi langkah 21 dan 22; TC-GS-GSET-18 a menjadi langkah 26, b menjadi langkah 28 dan 32, c menjadi langkah 30, d menjadi langkah 34 dan 35.
- TC-GS-GSET-16 langkah 2 (Klik `[Next]` ke Step 2) dipenuhi langkah 8 (walkthrough masih di Step 2 dari TC-GS-GSET-15) sehingga tidak diulang. TC-GS-GSET-16 dan 18 berdependensi TC-GS-GSET-14, yang berada di spec 010; precondition "flag belum ada" dipenuhi langkah 1 dan 24.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 24 (reset flag), dan 23 (menutup walkthrough replay); langkah 2 dan 25 adalah pembukaan halaman kunjungan pertama (aksi TC). Tooltip box, fokus, dan step diasersi segera setelah pemicunya (butir 5 bagian 8b).
- Verifikasi flag lewat API (langkah 19, 22, dan 35) dipakai karena Expected menyatakan flag `seen` tersimpan; kemampuan membacanya disediakan tim FE/BE.
- Temuan untuk QA:
  - TC-GS-GSET-15 sampai 18 tidak menyebut mekanisme menghapus atau membaca flag `seen` (Q-10); ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-GS-GSET-18 langkah 2 ("Tekan `→` (atau `Enter`)") ambigu; spec menekan keduanya pada dua kesempatan (langkah 27 dan 31) agar Expected b `→`/`Enter` keduanya teramati.
  - Email akun Total Control baru (Pre-setup No 8) tidak tertulis; spec memakai akun No 1 dengan flag dihapus.
