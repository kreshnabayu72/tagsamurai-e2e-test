---
id: TC-FA-NOTIF-E2E-045-tab-dan-search-dasar
title: "Tab All dan Unread serta Search Dasar Notification Center"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-183
  - TC-FA-NOTIF-184
  - TC-FA-NOTIF-185
  - TC-FA-NOTIF-186
  - TC-FA-NOTIF-187
  - TC-FA-NOTIF-425
coverage:
  web: automated
---

# Tab All dan Unread serta Search Dasar Notification Center

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi, termasuk N-06 dan N-07 berstatus Read), dipulihkan fixture BE pemulih di hook `before` dan `after`. Spec hanya membaca data. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>` (fixture belum ada; disediakan tim FE).
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed.

## Test Steps

### TC-FA-NOTIF-183: Tab All menampilkan seluruh notifikasi read dan unread sebagai default

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Verifikasi Tab `All` aktif
3. Verifikasi list memuat notifikasi Read dan Unread
4. Verifikasi list berurutan Newest (terbaru di atas)

### TC-FA-NOTIF-184: Tab Unread hanya menampilkan notifikasi belum dibaca

5. Klik Tab `Unread`
6. Scroll sampai akhir list hingga seluruh item termuat
7. Verifikasi list memuat sedikitnya satu item
8. Verifikasi setiap item pada list berstatus Unread
9. Verifikasi N-06 (`Your request has been rejected`) dan N-07 (`New audit task started`) tidak tampil

### TC-FA-NOTIF-185: Tab bukan opsi Filter: Filter Panel tidak memuat Read/Unread

10. Klik Bell icon, lalu klik `[Show All]` (kembali ke Tab All)
11. Klik icon Filter
12. Verifikasi Filter Panel memuat field `Event Type` dan `Date`
13. Verifikasi tidak ada field status Read/Unread pada Filter Panel
14. Klik icon Filter untuk menutup panel

### TC-FA-NOTIF-186: Search, Filter, dan Sort tetap berlaku saat berpindah antara Tab All dan Unread

15. Ketik Search `Waiting`, tekan Enter
16. Klik toggle Sort hingga Sort `Oldest`
17. Klik icon Filter, pilih Event Type `Borrow Waiting Approval`, lalu klik `[Apply]`
18. Klik Tab `Unread`
19. Verifikasi kotak Search tetap berisi `Waiting`
20. Verifikasi Sort `Oldest` tetap aktif
21. Verifikasi indikator titik pada icon Filter tampil (Filter tetap terpasang)
22. Verifikasi list memuat sedikitnya satu item
23. Verifikasi setiap item pada list berstatus Unread
24. Klik Tab `All`
25. Verifikasi kotak Search tetap berisi `Waiting`
26. Verifikasi Sort `Oldest` tetap aktif
27. Verifikasi indikator titik pada icon Filter tampil (Filter tetap terpasang)

### TC-FA-NOTIF-187: Search tanpa hasil pada Tab All menampilkan empty state filtered S-07

28. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
29. Ketik Search `zzzzzz`, tekan Enter
30. Verifikasi empty state tampil dengan Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`

### TC-FA-NOTIF-425: Search tanpa hasil pada Tab Unread menampilkan empty state filtered S-07, bukan S-02

31. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
32. Klik Tab `Unread`
33. Ketik Search `zzzzzz`, tekan Enter
34. Verifikasi empty state tampil dengan Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`
35. Verifikasi Title `No unread notifications` tidak tampil
36. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (precondition TC), 6 (memuat seluruh item agar asersi universal langkah 8 mencakup semua item), 10, 28, 31, 36 (masuk kembali lewat `[Show All]` yang mereset kontrol ke default; perilaku reset ini diasersi spec 114), 14 (menutup panel), 32.
- Asersi tambahan (S-03): langkah 7 (item pembanding sebelum asersi universal, 8b butir 2); langkah 22 (item pembanding sebelum asersi universal langkah 23, 8b butir 2); langkah 23 memeriksa set data Tab Unread.
- Alasan melewati ambang 35 langkah (36 langkah): keenam TC satu topik (Tab dan Search dasar Notification Center) pada akun dan seed yang sama, hanya membaca data; tiap TC berdiri sendiri dengan reset eksplisit lewat `[Show All]`.
- Temuan untuk QA:
  - TC-186 menulis "hanya set data yang berubah mengikuti tab" tanpa oracle set data; spec hanya mengasersi persistensi kontrol dan, pada Tab Unread, bahwa semua item berstatus Unread.
  - TC-184 menyebut N-06 dan N-07 sebagai item Read; judul N-07 diambil dari Pre-setup #17.
