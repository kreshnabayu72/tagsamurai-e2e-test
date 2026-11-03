---
id: TC-FA-SU-E2E-006-guided-tooltip-user-list-kunjungan-pertama-navigasi-replay-dan-exit
title: "Guided Tooltip User List: Kunjungan Pertama, Navigasi, Replay, dan Exit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-17
  - TC-FA-SU-18
  - TC-FA-SU-19
coverage:
  web: automated
---

# Guided Tooltip User List: Kunjungan Pertama, Navigasi, Replay, dan Exit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Pengecualian hook suite untuk flag Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-user` menjadi `seen`; spec ini menghapus flag itu pada akun aktor (setara akun baru tanpa flag) di langkah yang tertulis sebagai "Hapus flag" lewat kemampuan reset flag yang disediakan tim FE/BE (mekanisme mengikuti `foundation/functions/guided-tooltip.md`), dan hook `after` suite memulihkan flag ke nilai awal.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20). Nilai teks walkthrough dibaca dari `Fixture.faSettingsUser.guidedTooltip` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: pembacaan flag `guided_tooltip_seen_fa-settings-user` (disediakan tim FE/BE); pengaturan ukuran viewport browser dan pemulihannya (langkah 40 dan 52); tombol keyboard Esc, Enter, panah kiri, dan panah kanan.
- State global: flag Guided Tooltip akun aktor dan ukuran viewport; dipulihkan langkah 52 dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-17: Guided Tooltip User List: muncul otomatis pada kunjungan pertama dengan 5 step

1. Hapus flag `guided_tooltip_seen_fa-settings-user` akun aktor lalu muat ulang halaman Settings > User
2. Verifikasi walkthrough muncul otomatis dari Step 1
3. Verifikasi Step 1 pada Sidebar Group Tree berjudul `Group Sidebar` dengan teks "Use the sidebar to filter users by group. Click a group node to see only users within that group and its children."
4. Verifikasi `[Back]` Hidden di Step 1
5. Klik `[Next]`
6. Verifikasi Step 2 pada Toolbar berjudul `Search & Filters` dengan teks "Use the search bar and filters to quickly narrow down the user list."
7. Klik `[Next]`
8. Verifikasi Step 3 pada kolom Active berjudul `Portal Access Switch` dengan teks "Toggle a user's access to the FAMS portal. Some rows may be locked and cannot be toggled — hover for details."
9. Klik `[Next]`
10. Verifikasi Step 4 pada kolom Role berjudul `Role Summary` dengan teks "Shows the roles each user has. Click the role count to view the breakdown."
11. Klik `[Next]`
12. Verifikasi Step 5 pada header kolom Actions berjudul `Table Columns` dengan teks "Choose which columns the table shows. The actions available for each user are in the same column."

### TC-FA-SU-18: Guided Tooltip: navigasi Back, Next, Done, Skip, dan flag seen

13. Verifikasi `[Next]` berubah menjadi `[Done]` tepat di Step 5
14. Verifikasi tooltip box dapat difokus
15. Tekan panah kiri (←)
16. Verifikasi walkthrough berpindah ke Step 4
17. Tekan Enter
18. Verifikasi walkthrough berpindah ke Step 5
19. Tekan Esc
20. Verifikasi walkthrough tertutup (Esc = Skip)
21. Verifikasi flag seen tersetel
22. Muat ulang halaman
23. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya (Table Tools tampil sebagai anchor permukaan)
24. Hapus flag akun aktor lalu muat ulang halaman
25. Klik `[Next]` empat kali sampai Step 5
26. Klik `[Back]` sekali
27. Klik `[Next]` sekali
28. Klik `[Done]`
29. Verifikasi walkthrough tertutup
30. Verifikasi flag seen tersetel
31. Hapus flag akun aktor lalu muat ulang halaman
32. Klik `[Skip]`
33. Verifikasi walkthrough tertutup
34. Verifikasi flag seen tersetel
35. Hapus flag akun aktor lalu muat ulang halaman
36. Klik overlay gelap
37. Verifikasi walkthrough tertutup
38. Verifikasi flag seen tersetel

### TC-FA-SU-19: Guided Tooltip replay lewat tombol `[?]` dan exit tanpa menyetel flag

39. Hapus flag akun aktor lalu muat ulang halaman
40. Ubah ukuran viewport browser di tengah walkthrough
41. Verifikasi walkthrough tertutup
42. Verifikasi flag seen tidak tersetel
43. Muat ulang halaman Settings > User
44. Verifikasi walkthrough muncul lagi dari Step 1
45. Klik `[Skip]`
46. Hover tombol `[?]`
47. Verifikasi tombol `[?]` tepat di kanan Breadcrumb dan tooltip menampilkan `Show guide`
48. Klik tombol `[?]`
49. Verifikasi walkthrough dimulai dari Step 1
50. Verifikasi flag seen tetap tersetel (klik `[?]` tidak mereset flag)
51. Tekan Esc
52. Pulihkan ukuran viewport ke semula
53. Klik nama `Budi Santoso`
54. Verifikasi halaman Detail User tidak memiliki walkthrough dan tombol `[?]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 24, 31, 35, dan 39 (menghapus flag dan memuat ulang supaya walkthrough kunjungan pertama muncul), langkah 22 dan 43 (muat ulang), langkah 45 dan 51 (menutup walkthrough), langkah 52 (memulihkan viewport, S-09). Langkah 53 mengambil Detail untuk Expected d TC-FA-SU-19.
- Walkthrough TC-FA-SU-17 berakhir di Step 5 sehingga TC-FA-SU-18 melanjutkan dari keadaan itu (langkah 13 sampai 21: Step 5, keyboard, Esc); `[Back]` Hidden di Step 1 (Expected a TC-FA-SU-18) diasersi di langkah 4 saat Step 1 tampil.
- Langkah 14 sampai 18 mengisi Expected d TC-FA-SU-18 (Esc = Skip, Enter = Next, ← = Back); tombol → (Next) tidak diuji terpisah dari Enter karena Expected TC menyebut "Enter atau →" sebagai satu pasangan perilaku Next.
- Langkah 36 (klik overlay gelap) mengisi Expected b TC-FA-SU-18 ("tombol atau klik overlay gelap"); Langkah Uji TC hanya menyebut `[Skip]`.
- Spec melewati sekitar 35 langkah (54 langkah). Seluruhnya satu kelas (Guided Tooltip User List, satu akun, tanpa mengubah data bisnis), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-FA-SU-17 dan 18 memakai "akun baru tanpa flag guided tooltip" sebagai precondition; spec memakai akun aktor dengan flag dihapus (kemampuan reset flag disediakan tim FE/BE) sehingga tidak ada akun baru.
  - TC-FA-SU-18 Langkah Uji 5 ("Ulangi dengan akun baru") dan Langkah Uji 6 ("Uji tombol Esc, Enter, panah") tidak merinci urutan; spec menyusunnya seperti di atas.
  - TC-FA-SU-19 Expected c menyebut "atau navigasi ke halaman lain di tengah walkthrough"; Langkah Uji TC hanya meresize viewport dan membuka User List lagi. Spec menguji resize dan muat ulang, dan tidak menguji navigasi ke halaman lain.
  - TC-FA-SU-19 Langkah Uji 3 ("Buka halaman User List lagi") tidak menyebut apakah lewat navigasi atau muat ulang; spec memakai muat ulang.
  - TC-FA-SU-17 Expected a menyebut kunjungan pertama berdasarkan flag yang belum ada; nama flag mengikuti Expected TC (`guided_tooltip_seen_fa-settings-user`).
