---
id: TC-GS-POS-E2E-008-no-access-role-ditolak
title: Role tanpa akses: tab Hidden dan direct URL ditolak
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-60
  - TC-GS-POS-62
coverage:
  web: automated
---

# Role tanpa akses: tab Hidden dan direct URL ditolak

## Prerequisites

- Spec ini menguji dua lapis penolakan yang berbeda dan keduanya wajib ada. Lapis pertama, tab
  Position tidak muncul di navigasi sehingga user tidak pernah punya jalan masuk. Lapis kedua,
  address bar diketik langsung tetap ditolak. Menguji hanya lapis pertama menyisakan celah di mana
  cukup menulis URL untuk melewati gate UI, yang persis yang dicemaskan TC-GS-POS-62.
- Actor adalah Role No Access, yaitu user yang `access_level`-nya bukan Read Only dan bukan Total
  Control, dan tidak punya capability Manage user and role. Keadaan ini berbeda dari Read Only dan
  dari Capability Read-Only yang diuji di spec 005; ketiganya punya matriks UI berbeda.
- Akun No Access hanya dipakai pada spec ini.
- `Spectra.env.ADMIN_USERNAME` dan `Spectra.env.ADMIN_PASSWORD` dipakai hanya sebagai pembanding,
  yaitu membuktikan bahwa URL yang sama bisa dimuat oleh akun yang berhak, sehingga kegagalan pada
  Role No Access bukan akibat URL yang salah tulis.
- `Fixture.globalSettingsPosition.url.path` adalah path `Global Settings > User > Position` yang
  dipakai pada langkah direct URL.
- `Fixture.globalSettingsPosition.url.positionTab` adalah path tab Position di dalam halaman User,
  dipakai sebagai pembanding di langkah 10 sampai 12.
- `Fixture.globalSettingsPosition.url.defaultRoute` adalah rute default setelah penolakan, yaitu
  halaman yang mendarat setelah akses tidak diberikan. Nilai persisnya bergantung pada cara FE
  mengimplementasikan redirect, dan spec ini hanya menuntut mendarat di halaman yang bukan tab
  Position.
- `Fixture.globalSettingsPosition.positions.population` berisi data Position milik tenant yang sama,
  supaya data yang tidak bolehnya terbaca benar-benar ada.

## Test Steps

### Tab Position Hidden total di navigasi

1. Login sebagai Role No Access
2. Verifikasi login berhasil dan halaman awal terbuka
3. Verifikasi halaman `Global Settings > User` dapat dibuka
4. Verifikasi tab User List tampil pada sub-tab bar
5. Verifikasi tab Position tidak muncul pada sub-tab bar
6. Verifikasi tidak ada tab Position pada sub-tab bar dalam keadaan disabled maupun hidden, yaitu
   tidak ada elemen tab Position sama sekali
7. Verifikasi tidak ada entry Position pada sidebar atau menu navigasi lain
8. Verifikasi halaman User yang tampil adalah tab User List, bukan Position
9. Verifikasi halaman User List tidak menampilkan data Position

### Direct URL ditolak

10. Login sebagai Total Control, lalu buka
    `Fixture.globalSettingsPosition.url.positionTab` untuk membuktikan path ini memang bisa dimuat
    oleh akun yang berhak
11. Verifikasi tab Position berhasil dimuat dan data Position tampil
12. Keluar dari akun Total Control
13. Login kembali sebagai Role No Access
14. Ketik `Fixture.globalSettingsPosition.url.path` langsung ke address bar
15. Verifikasi halaman tidak menampilkan daftar data Position
16. Verifikasi tidak ada baris Position yang tampil, termasuk pada baris pertama
17. Verifikasi tidak ada detail Position yang terbuka
18. Verifikasi tidak ada toast sukses, karena tidak ada aksi yang diminta untuk sukses
19. Verifikasi halaman mendarat di `Fixture.globalSettingsPosition.url.defaultRoute`
20. Verifikasi halaman yang tampil bukan tab Position
21. Verifikasi tidak ada kontrol mutasi Position yang tampil, karena halaman Position tidak berhasil
    dimuat
22. Verifikasi tidak ada data Position yang bocor lewat pesan error, judul halaman, atau elemen
    lain di halaman tujuan

### Penolakan berulang tidak merusak state sesi

23. Pastikan masih login sebagai Role No Access setelah dua penolakan sebelumnya
24. Ulangi langkah 14 sampai 16 untuk memastikan penolakan konsisten dan bukan hanya terjadi sekali
25. Verifikasi sesi masih dalam status login dan tidak terputus
26. Verifikasi navigasi ke halaman lain yang memang berhak diakses masih berfungsi normal
27. Verifikasi tidak ada error yang tertinggal atau toast error yang menggantung di layar

## Notes

- Bandingkan dengan Role Read Only dan Capability Read-Only di spec 005. Ketiganya harus punya
  perilaku berbeda; kalau No Access ternyata punya matriks sama dengan Read Only, berarti ada bug
  pada pemetaan `access_level`. Karena itu spec ini tidak digabung ke spec 005.
- Langkah 10 sampai 12 adalah pembanding wajib. Tanpa membuktikan URL-nya benar, penolakan pada
  langkah 15 bisa terjadi karena path yang salah ketik, bukan karena permission, dan test akan
  lulus untuk alasan yang salah.
- Langkah 15 sampai 22 sengaja memisahkan setiap kebocoran yang mungkin, yaitu data di tabel,
  detail, toast sukses, kontrol mutasi, dan pesan error. Satu asersi gabungannya akan menutup
  sebagian kegagalan tanpa memberi tahu bagian mana yang bocor.
- Tidak ada ekspektasi kode status tertentu pada langkah 15. PRD §4.8 hanya menyebut ditolak atau
  redirect ke halaman default atau 403 page, jadi spec ini menuntut akibat yang dilihat pengguna
  dan tidak mengarang kode status yang tidak ditetapkan PRD.
- `Fixture.globalSettingsPosition.url.defaultRoute` ditulis naratif karena rute persisnya belum
  ditetapkan di PRD. Saat tahap script, nilainya diambil dari fixture, bukan ditebak.
- Subbagian ketiga sengaja diulang setelah dua penolakan untuk memastikan penolakan tidak merusak
  sesi. Penolakan yang mengakhiri sesi akan membuat pengguna logout paksa setiap kali salah
  ketik URL.
