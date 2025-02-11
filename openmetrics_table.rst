=========================================== ========================================================================== ======= ======= ================= ==============================================================================
Name                                        Description                                                                Type    Unit    Labels            Reference
=========================================== ========================================================================== ======= ======= ================= ==============================================================================
halon_cluster_connected                     The current connection status (true=1, false=0)                            gauge
halon_cluster_hosts                         Number of peers in the cluster                                             gauge
halon_process_license_expiration            License expiration                                                         counter seconds
halon_process_pid                           Process PID                                                                gauge                             `smtpd`
halon_process_runtime                       Process runtime                                                            counter seconds                   `smtpd`
halon_process_version_major                 Major version                                                              counter
halon_process_version_minor                 Minor version                                                              counter
halon_process_version_patch                 Patch version                                                              counter
halon_queue_connections_concurrent          Number of open connections                                                 gauge                             :confval:`queues.concurrency.total`
halon_queue_connections_maxconcurrent       Configured maximum number of open connections                              counter                           :confval:`queues.concurrency.total`
halon_queue_connections_pooling_evicts      Number of connections expired from the connection cache, due to size       counter
halon_queue_connections_pooling_expires     Number of connections expired from the connection cache, due to TTL        counter                           :ref:`idle timeout <queue_delivery>`
halon_queue_connections_pooling_hits        Number of connections reused in the connection cache                       counter
halon_queue_connections_pooling_maxsize     Configured maximum number of connections in the connection cache           counter                           :confval:`queues.pooling.size`
halon_queue_connections_pooling_misses      Number of connections not found in the connection cache                    counter
halon_queue_connections_pooling_size        Number of connections in the connection cache                              gauge                             :confval:`queues.pooling.size`
halon_queue_connections_pooling_skips       Number of connections not added to the connection cache, due to being full counter                           :ref:`non-evictable <queue_delivery>`
halon_queue_delivery_delayed                Number of soft-failed delivery events                                      counter
halon_queue_delivery_delivered              Number of messages successfully delivered                                  counter
halon_queue_delivery_failed                 Number of hard-failed delivery events                                      counter
halon_queue_freeze_hold_size                Number of messages in the hold queue                                       gauge
halon_queue_freeze_update_pending           Number of pending messages to be added to the update queue                 gauge                             :ref:`frozen for update <halonctl-queue-freeze>`
halon_queue_freeze_update_size              Number of messages in the update queue                                     gauge                             :ref:`frozen for update <halonctl-queue-freeze>`
halon_queue_loader_active                   Number of messages loaded in memory                                        gauge
halon_queue_loader_count                    Cumulative number of messages loaded into memory                           counter                           :doc:`queue <queue>`
halon_queue_loader_maxactive                Maximum number of messages loaded in memory                                counter                           :confval:`queues.maxmessages`
halon_queue_loader_pending                  Number of pending messages to be loaded into memory                        gauge
halon_queue_pickup_count                    Number of messages picked up from the active queue                         counter
halon_queue_pickup_evals                    The suspend evaluations against the list of suspends                       counter
halon_queue_pickup_misses                   Number of times the queue was searched without any message to deliver      counter
halon_queue_pickup_pending                  Number of messages picked up from the queue pending for delivery           gauge
halon_queue_pickup_putback                  Number of times a picked up message was put back into the queue            counter
halon_queue_pickup_skips                    Number of queue nodes skipped during message pickup                        counter
halon_queue_policy_concurrency_counters     Number of concurrency counters                                             gauge                             :ref:`active queue policies <queue_policy>`
halon_queue_policy_concurrency_suspends     Number of suspended concurrency counters                                   gauge                             :ref:`Suspensions <queue_suspend>` created as a result of exceeded concurrency
halon_queue_policy_connectinterval_buckets  Number of connect interval buckets active for the current queue            gauge
halon_queue_policy_connectinterval_suspends Number of suspended connect interval buckets                               gauge
halon_queue_policy_dynamic_conditions       Number of dynamically added policies                                       gauge                             script_
halon_queue_policy_dynamic_suspends         Number of dynamically added suspensions                                    gauge                             script_
halon_queue_policy_rate_buckets             Number of rate buckets active for the current queue                        gauge                             :ref:`active queue policies <queue_policy>`
halon_queue_policy_rate_suspends            Number of suspended rate buckets                                           gauge                             :ref:`Suspensions <queue_suspend>` created as a result of exceeded rate
halon_queue_queue_active_priorities_size    Number of messages in the active queue based on priorities                 gauge           priority          :doc:`queue <queue>`
halon_queue_queue_active_size               Number of messages in the active queue                                     gauge                             :doc:`queue <queue>`
halon_queue_queue_defer_size                Number of messages in the deferred queue                                   gauge                             :doc:`queue <queue>`
halon_queue_quota_size                      Number of quota counters                                                   gauge
halon_queue_release_pending                 Number of messages pending to be queued to run the post-delivery script    gauge
halon_queue_scripts_postdelivery_errors     Number of erroneous script executions (postdelivery)                       counter         threadid
halon_queue_scripts_postdelivery_finished   Number of finished script executions (postdelivery)                        counter         threadid
halon_queue_scripts_postdelivery_pending    Number of pending script executions (postdelivery)                         gauge           threadid
halon_queue_scripts_postdelivery_running    Number of running script executions (postdelivery)                         gauge           threadid
halon_queue_scripts_postdelivery_suspended  Number of suspended script executions (postdelivery)                       gauge           threadid
halon_queue_scripts_postdelivery_threads    Number of threads utilized for script executions (postdelivery)            gauge           threadid
halon_queue_scripts_predelivery_errors      Number of erroneous script executions (predelivery)                        counter         threadid
halon_queue_scripts_predelivery_finished    Number of finished script executions (predelivery)                         counter         threadid
halon_queue_scripts_predelivery_pending     Number of pending script executions (predelivery)                          gauge           threadid          :confval:`scripting.hooks.predelivery`
halon_queue_scripts_predelivery_running     Number of running script executions (predelivery)                          gauge           threadid          :confval:`queues.threads.script`
halon_queue_scripts_predelivery_suspended   Number of suspended script executions (predelivery)                        gauge           threadid
halon_queue_scripts_predelivery_threads     Number of threads utilized for script executions (predelivery)             gauge           threadid
halon_resolver_cache_evicts                 Number of entries expired from the DNS query cache, due to cache size      counter
halon_resolver_cache_expires                Number of entries expired from the DNS query cache, due to TTL             counter                           :confval:`resolver.cache.ttl.min`
halon_resolver_cache_hits                   Number of DNS query cache hits                                             counter
halon_resolver_cache_maxsize                Configured maximum number of entries in the DNS query cache                counter                           :confval:`resolver.cache.size`
halon_resolver_cache_misses                 Number of DNS query cache misses                                           counter
halon_resolver_cache_size                   Number of entries in the DNS query cache                                   gauge                             :confval:`resolver.cache.size`
halon_resolver_cache_skips                  Number of entries not added to the DNS query cached (eg. bad responses)    counter
halon_resolver_dedup                        Number of duplicate pending DNS queries                                    gauge
halon_resolver_domain_cache_evicts          Number of entries evicted from the domain cache, due to cache size         counter
halon_resolver_domain_cache_expires         Number of entries expired from the domain cache, due to TTL                counter
halon_resolver_domain_cache_hits            Number of domain cache hits                                                counter
halon_resolver_domain_cache_maxsize         Configured maximum number of entries in the domain cache                   counter
halon_resolver_domain_cache_misses          Number of domain cache misses                                              counter
halon_resolver_domain_cache_size            Number of entries in the domain cache                                      gauge
halon_resolver_maxrunning                   Configured maximum number of running DNS queries                           counter                           :confval:`resolver.concurrency`
halon_resolver_pending                      Number of pending DNS queries                                              gauge
halon_resolver_running                      Number of running DNS queries                                              gauge                             :confval:`resolver.concurrency`
halon_servers_connections_concurrent        Number of open connections                                                 gauge           serverid          :confval:`servers[].concurrency.total`
halon_servers_connections_maxconcurrent     Configured maximum number of open connections                              counter         serverid          :confval:`servers[].concurrency.total`
halon_servers_scripts_auth_errors           Number of erroneous script executions (AUTH)                               counter         serverid,threadid
halon_servers_scripts_auth_finished         Number of finished script executions (AUTH)                                counter         serverid,threadid
halon_servers_scripts_auth_pending          Number of pending script executions (AUTH)                                 gauge           serverid,threadid
halon_servers_scripts_auth_running          Number of running script executions (AUTH)                                 gauge           serverid,threadid
halon_servers_scripts_auth_suspended        Number of suspended script executions (AUTH)                               gauge           serverid,threadid
halon_servers_scripts_auth_threads          Number of threads utilized for script executions (AUTH)                    gauge           serverid,threadid
halon_servers_scripts_connect_errors        Number of erroneous script executions (connect)                            counter         serverid,threadid
halon_servers_scripts_connect_finished      Number of finished script executions (connect)                             counter         serverid,threadid
halon_servers_scripts_connect_pending       Number of pending script executions (connect)                              gauge           serverid,threadid :confval:`servers[].phases.connect.hook`
halon_servers_scripts_connect_running       Number of running script executions (connect)                              gauge           serverid,threadid :confval:`servers[].threads.script`
halon_servers_scripts_connect_suspended     Number of suspended script executions (connect)                            gauge           serverid,threadid
halon_servers_scripts_connect_threads       Number of threads utilized for script executions (connect)                 gauge           serverid,threadid
halon_servers_scripts_disconnect_errors     Number of erroneous script executions (disconnect)                         counter         serverid,threadid
halon_servers_scripts_disconnect_finished   Number of finished script executions (disconnect)                          counter         serverid,threadid
halon_servers_scripts_disconnect_pending    Number of pending script executions (disconnect)                           gauge           serverid,threadid
halon_servers_scripts_disconnect_running    Number of running script executions (disconnect)                           gauge           serverid,threadid
halon_servers_scripts_disconnect_suspended  Number of suspended script executions (disconnect)                         gauge           serverid,threadid
halon_servers_scripts_disconnect_threads    Number of threads utilized for script executions (disconnect)              gauge           serverid,threadid
halon_servers_scripts_eod_errors            Number of erroneous script executions (EOD)                                counter         serverid,threadid
halon_servers_scripts_eod_finished          Number of finished script executions (EOD)                                 counter         serverid,threadid
halon_servers_scripts_eod_pending           Number of pending script executions (EOD)                                  gauge           serverid,threadid
halon_servers_scripts_eod_running           Number of running script executions (EOD)                                  gauge           serverid,threadid
halon_servers_scripts_eod_suspended         Number of suspended script executions (EOD)                                gauge           serverid,threadid
halon_servers_scripts_eod_threads           Number of threads utilized for script executions (EOD)                     gauge           serverid,threadid
halon_servers_scripts_helo_errors           Number of erroneous script executions (HELO)                               counter         serverid,threadid
halon_servers_scripts_helo_finished         Number of finished script executions (HELO)                                counter         serverid,threadid
halon_servers_scripts_helo_pending          Number of pending script executions (HELO)                                 gauge           serverid,threadid
halon_servers_scripts_helo_running          Number of running script executions (HELO)                                 gauge           serverid,threadid
halon_servers_scripts_helo_suspended        Number of suspended script executions (HELO)                               gauge           serverid,threadid
halon_servers_scripts_helo_threads          Number of threads utilized for script executions (HELO)                    gauge           serverid,threadid
halon_servers_scripts_mailfrom_errors       Number of erroneous script executions (MAILFROM)                           counter         serverid,threadid
halon_servers_scripts_mailfrom_finished     Number of finished script executions (MAILFROM)                            counter         serverid,threadid
halon_servers_scripts_mailfrom_pending      Number of pending script executions (MAILFROM)                             gauge           serverid,threadid
halon_servers_scripts_mailfrom_running      Number of running script executions (MAILFROM)                             gauge           serverid,threadid
halon_servers_scripts_mailfrom_suspended    Number of suspended script executions (MAILFROM)                           gauge           serverid,threadid
halon_servers_scripts_mailfrom_threads      Number of threads utilized for script executions (MAILFROM)                gauge           serverid,threadid
halon_servers_scripts_proxy_errors          Number of erroneous script executions (proxy)                              counter         serverid,threadid
halon_servers_scripts_proxy_finished        Number of finished script executions (proxy)                               counter         serverid,threadid
halon_servers_scripts_proxy_pending         Number of pending script executions (proxy)                                gauge           serverid,threadid
halon_servers_scripts_proxy_running         Number of running script executions (proxy)                                gauge           serverid,threadid
halon_servers_scripts_proxy_suspended       Number of suspended script executions (proxy)                              gauge           serverid,threadid
halon_servers_scripts_proxy_threads         Number of threads utilized for script executions (proxy)                   gauge           serverid,threadid
halon_servers_scripts_rcptto_errors         Number of erroneous script executions (RCPTTO)                             counter         serverid,threadid
halon_servers_scripts_rcptto_finished       Number of finished script executions (RCPTTO)                              counter         serverid,threadid
halon_servers_scripts_rcptto_pending        Number of pending script executions (RCPTTO)                               gauge           serverid,threadid
halon_servers_scripts_rcptto_running        Number of running script executions (RCPTTO)                               gauge           serverid,threadid
halon_servers_scripts_rcptto_suspended      Number of suspended script executions (RCPTTO)                             gauge           serverid,threadid
halon_servers_scripts_rcptto_threads        Number of threads utilized for script executions (RCPTTO)                  gauge           serverid,threadid
halon_threads_scripts_maxrunning            Configured maximum number of threads that can run script executions        counter         id
halon_threads_scripts_maxscripts            Configured maximum number of script executions started (M:N)               counter         id
halon_threads_scripts_pending               Number of pending script executions                                        gauge           id
halon_threads_scripts_rescheduled           Number of rescheduled script executions                                    gauge           id
halon_threads_scripts_running               Number of threads running scripts executions                               gauge           id
halon_threads_scripts_scripts               Number of script executions to be started (M:N)                            gauge           id
=========================================== ========================================================================== ======= ======= ================= ==============================================================================
