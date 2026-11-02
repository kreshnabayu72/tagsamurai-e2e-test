---
id: TC-FA-GRP-E2E-043-konflik-dua-admin-create-tepat-di-cap-dan-re-check-atomik-saat-submit
title: "Konflik Dua Admin: Create Tepat di Cap dan Re-Check Atomik Saat Submit (Plan Growth dan Batas Platform)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-119
  - TC-FA-GRP-123
  - TC-FA-GRP-124
  - TC-FA-GRP-974
coverage:
  web: automated
---

# Konflik Dua Admin: Create Tepat di Cap dan Re-Check Atomik Saat Submit (Plan Growth dan Batas Platform)

## Prerequisites

- Mode: FE+BE (backend nyata; kelas c multi-konteks: dua admin menekan [Submit] bersamaan pada TC-FA-GRP-123 dan TC-FA-GRP-124; TC-FA-GRP-119 dan TC-FA-GRP-974 memakai pelaku kedua lewat sesi API).
- Akun aktor: Total Control A client Growth (cap 3), `Spectra.env.FA_GROWTH_TC_PASSWORD`; Total Control B client Growth (konteks UI kedua, TC-FA-GRP-123), `Spectra.env.FA_GROWTH_TC_B_PASSWORD`; Total Control A client Enterprise, `Spectra.env.FA_ENTERPRISE_TC_PASSWORD`; Total Control B client Enterprise (konteks UI kedua, TC-FA-GRP-124), `Spectra.env.FA_ENTERPRISE_TC_B_PASSWORD`. Semua nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; email keempat akun tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Login Total Control A client Growth di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite; akun client Enterprise lewat langkah ganti akun eksplisit (30); konteks UI kedua dibuka dan ditutup lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data client (disediakan tim FE): client Growth berisi tepat 2 group (precondition TC-FA-GRP-119, 974, dan 123); client Enterprise dengan Master Data Count Limit yang dapat diturunkan (TC-FA-GRP-124).
- Data Dinamis bersuffix `{runId}-043`: `Race Fill {runId}-043` (group pemicu dari sesi API), `Race Group {runId}-043`, `Race Close {runId}-043`, `Race A {runId}-043`, `Race B {runId}-043`, `Limit A {runId}-043`, `Limit B {runId}-043`; nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas fixture belum ada, dibuat di tahap script).
- State global yang diubah: Master Data Count Limit client Enterprise diturunkan menjadi jumlah group + 1 (langkah 31) dan dipulihkan di langkah 37 serta di hook `after`; pelaku dan mekanismenya disediakan tim FE/BE. Suite berjalan serial (`parallel: false`). Antar blok TC-FA-GRP-119, 974, dan 123 jumlah group client Growth dikembalikan ke 2 lewat API (langkah penghubung).
- Kemampuan teknis: sesi API aktor untuk membuat dan menghapus group sebagai pemicu; dua konteks browser terpisah (A dan B) yang menekan [Submit] bersamaan; pembacaan status respons simpan (409 Conflict) lewat intercept pasif atau fixture BE (disediakan tim FE); pembacaan jumlah group lewat fixture BE (disediakan tim FE/BE).
- Pemulihan (hook `after`): hapus lewat API semua group dengan suffix `{runId}-043`; pulihkan Master Data Count Limit; tutup konteks UI B; kembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-GRP-119: Re-check atomik saat Submit (cap tercapai setelah popup terbuka)

1. Klik [+] Group di konteks A (popup terbuka)
2. Lewat sesi API aktor, buat group `Race Fill {runId}-043` hingga jumlah group client Growth = 3 tersimpan
3. Di konteks A, isi Group Name `Race Group {runId}-043`, lalu klik [Submit]
4. Verifikasi konteks A ditolak server sebagai konflik (`409 Conflict`)
5. Verifikasi konteks A menampilkan dialog 🔒 `Cannot Add Group` dengan Body `You've reached the group limit for your plan. Upgrade to add more.` dan tombol hanya [OK] di atas popup form
6. Klik [OK]
7. Verifikasi dialog dan popup form tertutup
8. Verifikasi state di-refresh: sidebar menampilkan `Race Fill {runId}-043` (jumlah group terbaru)
9. Verifikasi `Race Group {runId}-043` tidak tersimpan
10. Hapus `Race Fill {runId}-043` lewat API hingga jumlah group client Growth = 2

### TC-FA-GRP-974: Race 409, [OK] menutup dialog dan popup form; Esc dan backdrop tidak menutup dialog

11. Klik [+] Group di konteks A (popup terbuka)
12. Lewat sesi API aktor, buat group `Race Fill {runId}-043` hingga jumlah group client Growth = 3 tersimpan
13. Di konteks A, isi Group Name `Race Close {runId}-043`, lalu klik [Submit]
14. Verifikasi dialog D-06 muncul di atas popup form dengan tombol hanya [OK]
15. Tekan Esc, lalu klik backdrop
16. Verifikasi dialog D-06 tetap tampil (Esc dan klik backdrop tidak menutup)
17. Klik [OK]
18. Verifikasi dialog dan popup form tertutup
19. Verifikasi state di-refresh: sidebar menampilkan `Race Fill {runId}-043`
20. Verifikasi `Race Close {runId}-043` tidak tersimpan
21. Hapus `Race Fill {runId}-043` lewat API hingga jumlah group client Growth = 2

### TC-FA-GRP-123: Create bersamaan tepat di cap, satu sukses dan satu ditolak

22. Buka konteks UI B dan login sebagai Total Control B client Growth
23. Konteks A dan B masing-masing klik [+] Group, A mengisi `Race A {runId}-043` dan B mengisi `Race B {runId}-043`
24. Konteks A dan B menekan [Submit] bersamaan
25. Verifikasi tepat satu konteks menampilkan toast sukses `Success, group has been created.`
26. Verifikasi konteks lainnya ditolak server `409 Conflict` dengan dialog plan gating D-06 di atas popup form
27. Pada konteks yang ditolak, klik [OK]
28. Verifikasi dialog dan popup form di konteks itu tertutup
29. Tutup konteks UI B dan hapus lewat API group yang tersimpan hingga jumlah group client Growth = 2

### Client Enterprise (TC-FA-GRP-124)

30. Ganti akun: logout konteks A, lalu login sebagai Total Control A client Enterprise; buka konteks UI B dan login sebagai Total Control B client Enterprise
31. Turunkan Master Data Count Limit di Lifecycle Settings > System Limits menjadi jumlah group client + 1 (tersisa 1 slot)
32. Konteks A dan B masing-masing klik [+] Group, A mengisi `Limit A {runId}-043` dan B mengisi `Limit B {runId}-043`, lalu keduanya menekan [Submit] bersamaan
33. Verifikasi tepat satu konteks sukses menyimpan group
34. Verifikasi konteks lainnya ditolak `409 Conflict` dengan dialog 🔒 `Cannot Add Group` (D-08) Body `You've reached the platform limit of [Group Limit] groups. Contact support if you need a higher limit.` dan tombol hanya [OK]
35. Pada konteks yang ditolak, klik [OK]
36. Verifikasi dialog dan popup form di konteks itu tertutup
37. Pulihkan Master Data Count Limit ke nilai awal dan tutup konteks UI B

## Notes

- Mode: FE+BE (backend nyata, kelas c multi-konteks; bagian 3 prinsip 13 butir c). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Pembagian TC lintas spec: TC-FA-GRP-190, 334, dan 335 (konflik dua admin pada Edit dan Code auto-generate, client Professional) ada di spec 279; spec ini hanya memuat konflik batas plan dan platform.
- Pelaku kedua pada TC-FA-GRP-119 dan 974 memakai sesi API aktor (bukan konteks UI kedua), sehingga tanpa butir `P-2`; konteks UI B hanya dibuka untuk TC-FA-GRP-123 dan TC-FA-GRP-124 karena hasilnya diasersi.
- TC-FA-GRP-123 dan TC-FA-GRP-124 non-deterministik pada konteks mana yang menang; asersi dirumuskan "tepat satu konteks" sukses dan konteks lainnya ditolak.
- Urutan blok: blok client Growth lebih dulu, lalu ganti akun ke client Enterprise (langkah 30); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah (b)). State dari blok sebelumnya (jumlah group = 3) dikembalikan ke 2 lewat API sebelum blok berikutnya (S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 10 (Hapus `Race Fill {runId}-043` lewat API hingga jumlah group client Gro...); langkah 21 (Hapus `Race Fill {runId}-043` lewat API hingga jumlah group client Gro...); langkah 22 (Buka konteks UI B dan login sebagai Total Control B client Growth); langkah 29 (Tutup konteks UI B dan hapus lewat API group yang tersimpan hingga jum...); langkah 30 (Ganti akun: logout konteks A, lalu login sebagai Total Control A clien...); langkah 31 (Turunkan Master Data Count Limit di Lifecycle Settings > System Limits...); langkah 37 (Pulihkan Master Data Count Limit ke nilai awal dan tutup konteks UI B).
- Alasan spec melewati ~35 langkah (37 langkah): seluruh blok satu kelas (multi-konteks race pada plan gating Create), tiap blok berdiri sendiri (precondition dibangun ulang lewat langkah penghubung), dan langkah banyak karena `Verifikasi` per klausa Expected (S-01).
- Temuan untuk QA:
  - Email dan password akun Total Control A dan B untuk client Growth dan Enterprise tidak tertulis di Pre-setup TC; spec memakai env baru dan akun yang disediakan tim FE.
  - TC-FA-GRP-119 dan TC-FA-GRP-974 Expected "state di-refresh (count terbaru)" tidak menyebut apa yang teramati; spec mengasersi bahwa sidebar menampilkan group pemicu dari sesi API.
  - TC-FA-GRP-124 tidak menyebut pelaku dan mekanisme penurunan Master Data Count Limit; dicatat sebagai kemampuan "disediakan tim FE/BE". `[Group Limit]` pada Expected diasersi sebagai nilai Master Data Count Limit yang diturunkan.
  - TC-FA-GRP-123 dan TC-FA-GRP-124 tidak menyebut konteks mana yang menang; asersi memakai "tepat satu".

