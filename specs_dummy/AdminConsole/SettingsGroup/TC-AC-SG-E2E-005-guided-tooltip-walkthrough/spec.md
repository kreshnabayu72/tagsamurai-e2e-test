---
id: TC-AC-SG-E2E-005-guided-tooltip-walkthrough
title: "Siklus lengkap Guided Tooltip kunjungan pertama, replay manual, dan tombol navigasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-163
  - TC-AC-SG-164
coverage:
  web: automated
---

# Siklus lengkap Guided Tooltip kunjungan pertama, replay manual, dan tombol navigasi

## Prerequisites

- Login sebagai Role: Total Control
- Flag user profile `guided_tooltip_seen_ac-settings-group` belum aktif (false / kunjungan pertama)

## Test Steps

### Kunjungan Pertama & Auto-Trigger
1. Buka halaman `Settings > Group` untuk pertama kali
2. Verifikasi walkthrough Guided Tooltip otomatis muncul dari Step 1
3. Verifikasi Step 1 menargetkan Sidebar Group Tree dengan Title `"Group Tree"` dan tombol `[Back]` tersembunyi (Hidden)
4. Klik `[Next]` menuju Step 2
5. Verifikasi Step 2 menargetkan Tabel Utama dengan Title `"Group Details"` dan tombol `[Back]` kini tampil
6. Klik `[Next]` menuju Step 3
7. Verifikasi Step 3 menargetkan tombol elipsis `[⋯]` pada baris tabel dengan Title `"Group Actions"`
8. Klik `[Next]` menuju Step 4
9. Verifikasi Step 4 menargetkan Toolbar TableTools (`[🔍 Search]` & `[⬇ Download]`) dengan Title `"Search & Export"`
10. Verifikasi pada Step 4 (step terakhir), tombol `[Next]` berubah label menjadi `[Done]`
11. Klik `[Done]` dan verifikasi walkthrough tertutup
### Kunjungan Kedua & Replay Manual
12. Refresh halaman `Settings > Group` (kunjungan kedua)
13. Verifikasi walkthrough Guided Tooltip TIDAK muncul secara otomatis
14. Klik tombol icon bantuan `[?]` di header halaman
15. Verifikasi walkthrough dimulai ulang dari Step 1
16. Klik tombol `[Skip]` (atau klik area backdrop overlay)
17. Verifikasi walkthrough tertutup seketika

## Notes

- Flag status dilihat disimpan di profil user setelah walkthrough diselesaikan atau di-skip.
