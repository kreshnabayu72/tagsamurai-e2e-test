---
id: TC-AC-PP-E2E-017-edit-screening-dan-jalur-masuk
title: "Screening Modal State Edit dan Dua Jalur Masuk ke State Edit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-41
  - TC-AC-PP-42
  - TC-AC-PP-43
coverage:
  web: automated
---

# Screening Modal State Edit dan Dua Jalur Masuk ke State Edit

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, Andi Wijaya, env `Spectra.env.AC_TC_PASSWORD`), login di hook `before`; hook `after` mengembalikan sesi ke akun default suite yang sama.
- Dataset Riwayat A di-seed di hook `before` lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat versi append-only) dan dikembalikan ke Riwayat A di hook `after`:
  - Version 3 Active, 10 Aug 2026 pukul 20:30 UTC, `John Doe`; isi: H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`.
  - Version 2 (02 Jul 2026, `John Doe`) dan Version 1 (15 Jan 2026, `Jane Smith`, akun sudah dihapus).
- Spec tidak mem-publish; semua modal Edit ditutup tanpa perubahan. Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).

## Test Steps

### TC-AC-PP-41: Row action Edit pada baris Active membuka Modal state Edit yang terisi konten versi Active

1. Buka Settings > Privacy Policy
2. Klik `[⋯]` pada baris `Version 3`
3. Pilih `Edit`
4. Tunggu konten termuat
5. Verifikasi `Settings > Privacy Policy > Popup Edit Privacy Policy` terbuka langsung di state Edit
6. Verifikasi info bar `Version 3 · Published At 10 Aug 26 · Published By John D`
7. Verifikasi editor terisi H1 `Privacy Policy`
8. Verifikasi editor terisi paragraf `This Privacy Policy describes how we collect, use, and protect your information.`
9. Verifikasi kursor fokus di awal konten
10. Verifikasi footer menampilkan `[Clear Field]`
11. Verifikasi footer menampilkan `[Publish New Version]`
12. Klik `[✕]` pada header modal
13. Tunggu modal tertutup

### TC-AC-PP-42: Tombol [Edit] di footer Modal View mengubah modal in-place ke state Edit

14. Klik teks tautan `Version 3`
15. Verifikasi Title modal "Privacy Policy Detail"
16. Klik `[Edit]` di footer
17. Tunggu konten termuat
18. Verifikasi modal yang sama berubah in-place ke state Edit tanpa tertutup
19. Verifikasi tidak ada navigasi halaman
20. Verifikasi Title berubah menjadi "Edit Privacy Policy"
21. Verifikasi info bar tetap `Version 3 · Published At 10 Aug 26 · Published By John D`
22. Verifikasi editor terisi konten versi Active
23. Verifikasi kursor fokus di awal konten
24. Verifikasi footer menampilkan `[Clear Field]`
25. Verifikasi footer menampilkan `[Publish New Version]`
26. Klik `[✕]` pada header modal
27. Tunggu modal kembali ke state View `Version 3`
28. Klik `[✕]` pada header modal

### TC-AC-PP-43: Screening Modal state Edit untuk versi Active yang sudah terisi

29. Klik `[⋯]` pada baris `Version 3`
30. Pilih `Edit`
31. Tunggu konten termuat
32. Susuri modal dari atas ke bawah tanpa mengklik apa pun
33. Verifikasi Header: Title modal "Edit Privacy Policy" (flat, tanpa nomor versi)
34. Verifikasi Header: tombol close `[✕]`
35. Verifikasi Header: info bar satu baris read-only `Version 3 · Published At 10 Aug 26 · Published By John D` (nomor versi Active hasil pengambilan server, bukan nomor versi yang akan terbit)
36. Verifikasi Published By pada info bar berupa komponen user dengan ikon user generik
37. Verifikasi Body: toolbar format berurutan `H1 | H2 | H3`, `B | I | U`, `• List | 1. List`, `Link`, `Undo | Redo`
38. Verifikasi Body: area editor terisi konten versi Active
39. Verifikasi Footer: `[Clear Field]` (text, primary) enabled
40. Verifikasi Footer: `[Publish New Version]` (Success) enabled
41. Verifikasi Footer: tidak ada tombol `[Cancel]`
42. Verifikasi Footer: tidak ada tombol Close
43. Klik `[✕]` pada header modal

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 12, 28, dan 43 menutup modal Edit yang bersih lewat `[✕]` (tanpa dialog). Langkah 26-27 adalah aksi tambahan agar kembali dari state Edit ke state View sebelum modal ditutup; tidak ada perubahan konten sehingga tidak ada dialog `Unsaved Changes`.
- Langkah 13 dan 27 adalah langkah penghubung tanpa `Verifikasi` (menunggu modal tertutup dan menunggu modal kembali ke state View `Version 3` sebelum langkah berikutnya); keduanya tidak menurunkan Expected TC-AC-PP-41/42 dan tidak dipakai sebagai bukti Post Condition. Perilaku penutupan bersih tanpa dialog (Expected TC-AC-PP-64) diasersi di spec penutupan modal Edit, bukan di sini.
- Langkah 15 (Title "Privacy Policy Detail" sebelum klik `[Edit]`) adalah asersi pendukung bagian pembanding "berubah dari ... menjadi" pada Expected b TC-AC-PP-42 (langkah 20).
- Spec melewati sekitar 35 langkah (43 langkah) tanpa pengecualian P-1/P-2/P-3; tidak dipecah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01), seluruh TC memakai satu dataset (Riwayat A) dan akun yang sama, tidak ada kelas harness lain, dan tiap blok `###` berdiri sendiri (dimulai dari tabel setelah langkah penghubung penutupan modal).
- Temuan untuk QA: TC-AC-PP-41 Expected c ("Kursor fokus di awal konten") tidak menyebut cara mengasersi posisi kursor; tim FE menentukan (mis. posisi seleksi editor di offset 0). Post Condition ketiga TC (tidak ada versi baru dan tidak ada record audit) tidak punya langkah observasi sehingga tidak diasersi.
