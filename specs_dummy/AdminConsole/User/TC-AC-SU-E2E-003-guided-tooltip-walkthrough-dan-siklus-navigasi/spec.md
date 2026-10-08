---
id: TC-AC-SU-E2E-003-guided-tooltip-walkthrough-dan-siklus-navigasi
title: "Guided Tooltip walkthrough 5 step, auto-trigger kunjungan pertama, manual replay, dan keyboard navigation"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-228
  - TC-AC-SU-229
  - TC-AC-SU-267
  - TC-AC-SU-268
coverage:
  web: automated
---

# Guided Tooltip walkthrough 5 step, auto-trigger kunjungan pertama, manual replay, dan keyboard navigation

## Prerequisites

- Login sebagai Role: Total Control
- Akun pengguna memiliki flag preferensi `guided_tooltip_seen_ac-settings-user = false` (kondisi kunjungan pertama)

## Test Steps

### Auto-Trigger Kunjungan Pertama & Screening Konten 5 Step
1. Buka menu `Admin Console > Settings > User` untuk pertama kali
2. Verifikasi walkthrough otomatis muncul menunjuk target Step 1 (Group Sidebar) dengan judul `"Group Sidebar"` dan tombol `[Back]` berstatus Hidden
3. Verifikasi teks deskripsi Step 1 cocok verbatim: `"Use the sidebar to filter users by group. Click a group node to see only users within that group and its children."`
4. Klik tombol `[Next]`
5. Verifikasi walkthrough berpindah ke Step 2 menunjuk toolbar Search & Filters dengan judul `"Search & Filters"`
6. Klik tombol `[Next]`
7. Verifikasi walkthrough berpindah ke Step 3 menunjuk kolom switch Active dengan judul `"Portal Access Switch"`
8. Klik tombol `[Next]`
9. Verifikasi walkthrough berpindah ke Step 4 menunjuk kolom Role dengan judul `"Role Summary"`
10. Klik tombol `[Next]`
11. Verifikasi walkthrough berpindah ke Step 5 menunjuk kolom row action `[⋯]` dengan judul `"User Actions"`, dan tombol `[Next]` berubah label menjadi `[Done]`
12. Klik tombol `[Done]`
13. Verifikasi walkthrough tertutup dan flag `guided_tooltip_seen_ac-settings-user` berubah menjadi `true`

### Kunjungan Kedua & Manual Replay
14. Refresh halaman atau navigasi keluar lalu kembali ke menu `Settings > User`
15. Verifikasi walkthrough TIDAK muncul secara otomatis pada kunjungan kedua
16. Klik tombol bantuan icon `[?]` pada header halaman
17. Verifikasi walkthrough mulai ulang secara manual dari Step 1 tanpa mereset flag permanent seen
18. Klik tombol `[Next]` hingga Step 3, lalu klik tombol `[Skip]`
19. Verifikasi walkthrough langsung tertutup

### Keyboard Navigation & Exit Tanpa Flag
20. Klik tombol `[?]` untuk membuka walkthrough lagi
21. Tekan tombol keyboard `Enter` dan verifikasi navigasi maju ke step berikutnya (setara tombol `[Next]`)
22. Tekan tombol panah kiri `←` dan verifikasi navigasi mundur ke step sebelumnya (setara tombol `[Back]`)
23. Tekan tombol `Esc` dan verifikasi walkthrough tertutup setara `[Skip]`
24. Atur ulang flag seen ke `false`, buka halaman, dan saat Step 1 aktif lakukan resize viewport browser secara drastis
25. Verifikasi walkthrough tertutup TANPA mengubah flag `seen` menjadi `true` sehingga walkthrough akan muncul kembali pada kunjungan berikutnya

## Notes

- Guided Tooltip membantu orientasi pengguna baru dan dapat dipanggil kembali kapan saja via tombol [?].
