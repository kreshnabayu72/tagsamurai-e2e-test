---
id: TC-AC-ACAL-E2E-007-role-matrix-positif-total-control-dan-read-only
title: "Role Matrix Positif — Akses menu dan kontrol penuh untuk Principal, Distributor, dan Partner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-23
  - TC-AC-ACAL-24
  - TC-AC-ACAL-25
  - TC-AC-ACAL-27
  - TC-AC-ACAL-28
coverage:
  web: automated
---

# Role Matrix Positif — Akses menu dan kontrol penuh untuk Principal, Distributor, dan Partner

## Prerequisites

- Akun uji untuk masing-masing role berikut:

| Role yang diuji | Entitas | Tipe Akses |
| :--- | :--- | :--- |
| Principal Total Control | Principal | Total Control |
| Principal Read Only | Principal | Read Only |
| Distributor Total Control | Distributor | Total Control |
| Distributor Read Only | Distributor | Read Only |
| Partner Total Control | Partner | Total Control |
| Partner Read Only | Partner | Read Only |

## Test Steps

Lakukan langkah berikut untuk setiap role pada tabel di atas:

1. Login menggunakan kredensial role yang sedang diuji
2. Amati sidebar navigasi Admin Console
3. Verifikasi menu `"Activity Log"` tampil (Show) dan dapat diklik
4. Buka menu `Admin Console > Activity Log`
5. Verifikasi halaman terbuka dengan sukses menampilkan Tab Session dan Tab User Action
6. Verifikasi seluruh kontrol toolbar (`Search`, `Filter`, `Download`, `Setup Column`) tampil dan dapat dioperasikan penuh
7. Verifikasi tidak ada perbedaan fungsional antara Total Control dan Read Only (karena modul ini read-only secara universal)
8. Logout sebelum beralih ke role berikutnya

## Notes

- Modul Activity Log bersifat read-only untuk seluruh pengguna berhak, sehingga pengguna Read Only memiliki kapabilitas melihat, menyaring, dan mengunduh yang setara dengan Total Control.
