---

id: TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final

title: "Defense-in-Depth: Edit, Cancel, dan Resubmit Milik Orang Lain dan pada Status Final"

priority: Critical

caseType: Negative

status: draft

sourceTc:

  - TC-AC-LA-82

  - TC-AC-LA-222

  - TC-AC-LA-199

  - TC-AC-LA-233

  - TC-AC-LA-200

  - TC-AC-LA-223

  - TC-AC-LA-234

coverage:

  web: automated

---



# Defense-in-Depth: Edit, Cancel, dan Resubmit Milik Orang Lain dan pada Status Final



## Prerequisites



- Mode: FE+BE.

- Akun aktor pertama: Group Manager approve-only `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rian Hartono`, Pre-setup #8), password `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

- Akun ganti akun (langkah eksplisit): Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`; Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`.

- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.

- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.

- Data Pre-setup (hanya dibaca; semua request ditolak sehingga tidak ada perubahan): PT Sejahtera (#19), Bengkel Cahaya Motor (#23), toggle Require Approval for Allocation ON (#38).

- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): alokasi `Waiting for Approval` Concurrent User +5 milik `Dewi A` (bentuk #41) untuk TC-AC-LA-222 dan TC-AC-LA-199; alokasi `Canceled` manual milik `Dewi A` (bentuk #48) untuk TC-AC-LA-233; satu seed per status final milik `Dewi A` untuk TC-AC-LA-200, 223, 234: `Active` (bentuk #47), `Rejected` (bentuk #50), `Canceled` manual (bentuk #48), `Expired` (bentuk #76). Allocation ID dibaca dari hasil seeding.

- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request submit, Edit, Cancel, dan Resubmit langsung ke server memakai sesi API akun aktor masing-masing (login API tidak dihitung sebagai sesi web, `suite.md`), membaca status dan jumlah record lewat fixture BE (tanpa mengarang endpoint, S-13).

- Tabel parameter blok status final (dipakai langkah 33 sampai 38):



| Status seed | Tab | TC-AC-LA-200 (Edit) | TC-AC-LA-223 (Cancel) | TC-AC-LA-234 (Resubmit) |

|---|---|---|---|---|

| `Active` | Current | ya | ya | ya |

| `Rejected` | History | ya | ya | ya |

| `Canceled` | History | ya | tidak | tidak |

| `Expired` | History | ya | ya | ya |



- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).



## Test Steps



### TC-AC-LA-82: Group Manager approve-only tidak dapat Allocate, Edit, atau Resubmit



1. Catat jumlah alokasi PT Sejahtera lewat fixture BE sebagai baseline, lalu periksa toolbar tab Current

2. Verifikasi Table Tools tampil di toolbar yang sama (anchor)
3. Verifikasi `[+ Allocation]` Hidden

4. Ketik Search Allocation ID seed `Waiting for Approval`, tekan Enter, lalu buka menu `⋯` pada baris itu
5. Verifikasi row action `Allocation Log` tampil pada menu `⋯` (anchor)
6. Verifikasi row action `Edit` Hidden
7. Verifikasi row action `Resubmit` Hidden
8. Tutup menu `⋯`, klik tab `History`, kosongkan kotak search: klik `✕` pada Search, tekan Enter, ketik Search Allocation ID seed Canceled, tekan Enter, lalu buka menu `⋯` pada baris Canceled
9. Verifikasi row action `Allocation Log` tampil pada menu `⋯` (anchor)
10. Verifikasi row action `Edit` Hidden
11. Verifikasi row action `Resubmit` Hidden




12. Kirim request submit alokasi langsung ke server dengan akun ini

13. Verifikasi respons server menolak dengan penolakan akses

14. Verifikasi tidak ada record baru (jumlah alokasi PT Sejahtera sama dengan baseline langkah 1)



### TC-AC-LA-222: Cancel oleh Group Manager pada Waiting for Approval milik orang lain



15. Tutup menu `⋯`, klik tab `Current`, kosongkan kotak search: klik `✕` pada Search, tekan Enter, ketik Search Allocation ID seed `Waiting for Approval` milik `Dewi A`, tekan Enter, lalu buka menu `⋯` pada baris itu

16. Verifikasi row action `Allocation Log` tampil pada menu `⋯` (anchor)

17. Verifikasi `Cancel Allocation` tidak tersedia

18. Kirim request Cancel langsung untuk record itu

19. Verifikasi respons server menolak

20. Verifikasi status record tidak berubah



### TC-AC-LA-199: Edit oleh selain requester original ditolak



21. Ganti akun: logout `Rian H`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`

22. Kirim request Edit langsung untuk record `Waiting for Approval` milik `Dewi A`

23. Verifikasi respons server menolak (aktor bukan requester original)

24. Verifikasi record tidak berubah



### TC-AC-LA-233: Resubmit oleh selain requester original ditolak



25. Buka Allocation > License Allocation

26. Klik tab `History`, ketik Search Allocation ID seed Canceled milik `Dewi A`, tekan Enter, lalu buka menu `⋯` pada baris itu

27. Verifikasi row action `Allocation Log` tampil pada menu `⋯` (anchor)

28. Verifikasi `Resubmit` tidak tersedia

29. Kirim request Resubmit langsung untuk record itu

30. Verifikasi respons server menolak

31. Verifikasi tidak ada record baru



### TC-AC-LA-200, TC-AC-LA-223, dan TC-AC-LA-234: Aksi pada record status final ditolak



32. Ganti akun: logout `Fajar N`, login sebagai `Dewi Anggraini` dengan `Spectra.env.AC_LA_DIST_FULL_PASSWORD`




Untuk setiap aksi (Edit, Cancel, Resubmit) dan setiap status seed yang bertanda "ya" pada tabel parameter (langkah 33 sampai 38):



33. Kirim request aksi langsung untuk record seed berstatus tersebut milik sendiri

34. Verifikasi respons server menolak (Edit dan Cancel: respons error generik; Resubmit: ditolak)

35. Verifikasi record tidak berubah (Edit dan Cancel) atau tidak ada record baru (Resubmit)

36. Buka Allocation > License Allocation, klik tab pada kolom Tab tabel parameter, ketik Search Allocation ID seed berstatus tersebut, tekan Enter, lalu buka menu `⋯` baris itu

37. Verifikasi row action `Allocation Log` tampil pada menu `⋯` (anchor)

38. Verifikasi row action aksi itu (`Edit`, `Cancel Allocation`, atau `Resubmit`) tidak tersedia



## Notes



- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan nomor agar semua TC satu akun berurutan sebelum ganti akun.

- K-1: TC kelas a yang Expected-nya respons API tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend. TC-AC-LA-82, 222, 233, 200, 223, 234 juga memuat bagian UI (visibilitas row action) yang diasersi di browser.

- Langkah 33 sampai 38 diulang untuk 4 status pada TC-AC-LA-200, 3 status pada TC-AC-LA-223, dan 3 status pada TC-AC-LA-234 (10 iterasi, 8b butir 7), parameter (status seed, tab tempat baris berada, dan TC yang berlaku) pada tabel Prerequisites. Setiap Verifikasi tetap satu per klausa.

- Langkah penghubung (S-03): langkah 4, 8, 15, 26, 36 (Search, tab, dan membuka menu `⋯` pada baris target, R-16; langkah 8 dan 15 menutup menu `⋯` dan mengosongkan kotak Search dengan klik `✕` lalu Enter sesudah pindah tab, S-09, S-14; langkah 36 membuka List pada awal tiap iterasi, termasuk iterasi pertama sesudah ganti akun, S-07, S-14), 21 dan 32 (ganti akun). Langkah 1 mencatat baseline (S-12).

- Asersi `Hidden` atau tidak tersedia (langkah 3, 6, 7, 10, 11, 17, 28, 38) beranchor Table Tools (langkah 2) dan Verifikasi row action `Allocation Log` tampil pada menu `⋯` yang sama (langkah 5, 9, 16, 27, 37; asersi tambahan di luar TC yang dicatat sesuai S-03 dan 8b butir 2; row action `Allocation Log` diandaikan tersedia karena akun uji punya akses baca List). Langkah 25 membuka List sesudah ganti akun sebelum langkah 26 membuka tab `History` (S-14).

- Spec melewati sekitar 35 langkah setelah ekspansi iterasi. Alasan pertahanan: seluruh blok satu kelas harness (defense-in-depth tanpa harness eksternal) pada topik yang sama (aksi tulis oleh bukan pemilik atau pada status final) dan tiap blok berdiri sendiri.

- Temuan untuk QA:

  - TC-AC-LA-82, 222, 199, 233, 200, 223, 234 menyebut "respons error generik" atau "penolakan akses" tanpa status HTTP; spec mengasersi penolakan tanpa kode.

  - TC-AC-LA-82 Langkah 1 ("Periksa toolbar") tidak menyebut baris tempat row action `Edit` dan `Resubmit` diperiksa; spec memakai baris `Waiting for Approval` dan Canceled.

  - TC-AC-LA-200 Precondition menyebut alokasi Expired milik `Dewi A` (Pre-setup #76) pada tab Current, padahal Expired berada di tab History; spec membuka baris di tab yang sesuai statusnya.

  - TC-AC-LA-223 dan TC-AC-LA-234 tidak menyebut status `Canceled` (TC-AC-LA-223: selain Canceled; TC-AC-LA-234: selain Canceled); tabel parameter mengikutinya.

